import getpass
import os
os.environ["OPENAI_API_KEY"] = getpass.getpass()


import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from llama_index.readers.s3 import S3Reader

    
class QandA:
    def ragLlama(bucketName):
        PERSIST_DIR = "./storage"
        if not os.path.exists(PERSIST_DIR):
            loader = S3Reader(
                bucket=bucketName,
            )
            documents = loader.load_data()
            index = VectorStoreIndex.from_documents(documents)
            index.storage_context.persist(persist_dir=PERSIST_DIR)
        else:
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)
        return index
        
    def QueryEngine(index,prompt):
        query_engine = index.as_query_engine()
        response = query_engine.query(prompt)
        return response