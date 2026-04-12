file_path = "/Volumes/workspace/default/demovol/dpact.pdf"
 
 
import fitz  # PyMuPDF
# Read file content
with open(file_path, "rb") as f:
    pdf_bytes = f.read()
 
# Use PyMuPDF to extract text
doc = fitz.open("pdf", pdf_bytes)
text = ""
for page in doc:
    text += page.get_text()
print(text)  # Print first 1000 characters
 
# CSV Example
df = spark.read.option("header", "true").csv("/Volumes/<catalog>/<schema>/<volume>/filename.csv")

# OR Parquet
# df = spark.read.parquet("/Volumes/<catalog>/<schema>/<volume>/filename.parquet")
 
# OR JSON
# df = spark.read.option("multiline", "true").json("/Volumes/<catalog>/<schema>/<volume>/filename.json")
 
 
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
# Load documents (e.g., text files or PDFs from DBFS or local)
raw_text = text
 # Replace this with your actual file reader logic
 
# Chunk documents for embedding
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = text_splitter.create_documents([raw_text])
len(docs)
docs[0]
docs[1]
 
import pandas as pd# Convert docs to a list of dicts for display
pd_docs = pd.DataFrame([doc.dict() for doc in docs])
pd_docs.insert(0, "id_pk", range(1, len(pd_docs) + 1))
display(pd_docs)