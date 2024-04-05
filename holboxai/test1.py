from s3_reader import S3DocReader
from csv_query import CsvQuery
import pandas as pd

# reader = S3DocReader()
# docs = reader.get_bucket("gen-ai-for-automotive")
# print(docs)

# ib = CsvQuery()
# query = "what is the total value"
# df = pd.read_csv("/home/ubuntu/RAG_API/csv_file/Air_Quality.csv")
# response = ib.single_csv_query(df, query)
# print(response) 


# Text Summarization 
from summarizer import Summarizer

reader = S3DocReader()
docs = reader.get_docs(bucket_name="gen-ai-for-healthcare",key = "Emerging Trends in Breast Cancer Care.txt")
doc_summary = Summarizer()
summary = doc_summary.summarize(docs)
print(summary)