from s3_reader import S3DocReader
from csv_query import CsvQuery
from docs_query import DocsQuery
import pandas as pd
from sentiment_analysis import SentimentAnalysis
from name_entity_recognition import NameEntityRecognition
from text2image import text2image
from summarizer import Summarizer
from relevant_docs import RelevantDocs

## S3 files Reader 

# reader = S3DocReader()
# docs = reader.get_docs("gen-ai-for-automotive")
# print(docs)

## RAG in S3 Documents : 

# docsQuery = DocsQuery()
# indexes = docsQuery.create_index(documents)
# query = " "  # Your query here
# response = docsQuery.query(indexes, query)

## Semantic Search 

# query = " "
# rel_docs = hb.RelevantDocs()
# docs = rel_docs.get_docs(query, n_docs=4, indexes)


## RAG in csv file

# ib = CsvQuery()
# query = "what is the total value"
# df = pd.read_csv("/home/ubuntu/RAG_API/csv_file/Air_Quality.csv")
# response = ib.single_csv_query(df, query)
# print(response) 


## Image generation 

# txt2img = text2image()
# prompt = "a sports car, on a racing track,4K" 
# txt2img.generate_image(prompt, 5, 25) # example : cfg_scale = 5 , inference_steps = 25 


## Document Summarization 

# reader = S3DocReader()
# docs = reader.get_file(bucket_name="<Bucket Name>",key = "<File Name>")
# doc_summary = Summarizer()
# summary = doc_summary.summarize(docs)
# print(summary)


## Sentiment Analysis on text

# Sentiment using cohere.command-text-v14

# sa = SentimentAnalysis()
# response1 = sa.get_sentiment("I'm extremely disappointed with the quality of the product. It broke after just one week of use.")
# print(response1)


# Sentiment using anthropic.claude-3-sonnet-20240229-v1:0

# response2 = sa.get_sentiment("I'm extremely disappointed with the quality of the product. It broke after just one week of use.", "anthropic.claude-3-sonnet-20240229-v1:0")
# print(response2)


# Sentiment using amazon.titan-text-express-v1

# response3 = sa.get_sentiment("I'm extremely disappointed with the quality of the product. It broke after just one week of use.", "amazon.titan-text-express-v1")
# print(response3)




## Name Entity Recognition

# Using cohere.command-text-v14

# ner = NameEntityRecognition()
# response = ner.get_entity("Harry and jay are going for a party in dubai, after that they will visit paris.")
# print(response)

# # Using anthropic.claude-3-sonnet-20240229-v1:0

# response = ner.get_entity("Harry and jay are going for a party in dubai, after that they will visit paris.", "anthropic.claude-3-sonnet-20240229-v1:0")
# print(response)

# # Using amazon.titan-text-express-v1

# response = ner.get_entity("Harry and jay are going for a party in dubai, after that they will visit paris.", "amazon.titan-text-express-v1")
# print(response)

