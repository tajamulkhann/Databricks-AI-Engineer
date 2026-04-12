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