# HolboxAI Package
Welcome to HolboxAI, a comprehensive AI package designed to enhance your data processing and creative capabilities. HolboxAI offers a range of functionalities including text-to-image generation, running textual queries on documents stored in your S3 bucket, and generating insights from natural language queries. This README provides a detailed guide on how to install and use the various features of HolboxAI.
Installation
To get started with HolboxAI, you need to install the package. Run the following command in your terminal:
```sh
pip install holboxai
```

This command installs all the functionalities of HolboxAI, including:
RAG Functionality - Running textual queries on the documents stored in your S3 bucket.
Generating images from text prompts.
Generating insights based on your natural language queries.
After installation, you can import HolboxAI into your project using:
```sh
import holbox as hb
```
## Features
### 1. RAG Functionality
To run textual queries on your S3 bucket documents, follow these steps:
Load Documents from S3 Bucket:
First, import the S3DocReader class and initialize it. Then, call the get_bucket() method and provide the name of your S3 bucket as its argument.
```sh
from holboxai.s3_reader import S3DocReader

reader = S3DocReader()
documents = reader.get_bucket("bucket_name")  # Pass the name of your bucket
```
#### Index Documents and Generate Response:
Next, import the DocsQuery class. Use createindexes() to index the documents and query() to generate the response for your prompted query.
```sh
from holboxai.docs_query import DocsQuery

docsQuery = DocsQuery()
indexes = docsQuery.createindexes(documents)
query = " "  # Your query here
response = docsQuery.query(indexes, query)
```
#### Validate Sources:
To validate the sources that generated the response of your query, import RelevantDocs and call get_docs(). This will show all the documents from which the response is created.
```sh
from holboxai.relevant_docs import RelevantDocs

rel_docs = RelevantDocs()
list_of_rel_docs = rel_docs.get_docs(query, num=4, indexes)
```
### 2. Generating Images from Text Prompts
To generate images based on your text prompts, use the text2image module. The generate_image() method's arguments include your desired prompt, guidance scale, and inference steps.
```sh
from holboxai.text2image import text2image

txt2img   = text2image()

prompt    = "a sports car, on a racing track, 4K" #Change the prompt according to requirement
cfg_scale = Guidance scale is a parameter that controls how much the image generation 
            process follows the text prompt. The higher the value, the more the image
            sticks to a given text input and vice-versa. It ranges from (1-20) 
inference_steps = Inference steps controls how many steps will be taken during this process. 
                  The higher the value, the more steps that are taken to produce the image.
                  It ranges from (5-100)

txt2img.generate_image(prompt, 5, 25) # example : cfg_scale = 5 , inference_steps = 25 
```
### 3. Generating Insights from CSV Files
HolboxAI also allows you to generate visual insights from CSV files. First, import csv_reader from holboxai.informabot, then call read_csv_file() providing the file path as its argument. Lastly, to generate the answer, call get_answer() with your query as the argument.
```sh
import holboxai as hb
import pandas as pd 
informabot = hb.CsvQuery()

query = "your query"
df = pd.read_csv("<path>")
response = informabot.single_csv_query(df , query)
print(response)
```
## Conclusion
HolboxAI is designed to simplify complex AI functionalities and make them accessible for various applications. Whether you're querying documents, generating creative images, or seeking insights from data, HolboxAI provides the tools you need. Enjoy exploring the capabilities of HolboxAI in your projects!