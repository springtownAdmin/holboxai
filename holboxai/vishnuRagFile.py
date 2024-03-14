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

class RagLlama:
    def rag():
        documents = SimpleDirectoryReader("The Witcher documents").load_data()
        index = VectorStoreIndex.from_documents(documents)

        query_engine_witcher = index.as_query_engine()

        response_witcher = query_engine_witcher.query("what is amazon bedrock")
        return response_witcher