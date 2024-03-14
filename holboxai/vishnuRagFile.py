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
class QandA:
    def ragLaama(st):
        PERSIST_DIR = "./storage"
        if not os.path.exists(PERSIST_DIR):
            documents = SimpleDirectoryReader("The Witcher documents").load_data()

            documen = documents
            index = VectorStoreIndex.from_documents(documents)
            index.storage_context.persist(persist_dir=PERSIST_DIR)
        else:
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)
            
        query_engine_witcher = index.as_query_engine()

        if(st!=None):
            response_witcher = query_engine_witcher.query(st)
        else:
            response_withcer = query_engine_witcher.query("Give a summary")

        return response_witcher