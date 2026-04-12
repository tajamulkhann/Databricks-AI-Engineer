%pip install -U --quiet databricks-sdk==0.49.0 "databricks-langchain>=0.4.0" databricks-agents mlflow[databricks] databricks-vectorsearch==0.55 langchain==0.3.25 langchain_core==0.3.59 bs4==0.0.2 markdownify==0.14.1 pydantic==2.10.1 mlflow openai PyMuPDF

dbutils.library.restartPython()

#make sure you have index in workspace.default.my_index or replace with your index name
from databricks_langchain import DatabricksVectorSearch
vector_store = DatabricksVectorSearch(index_name="workspace.default.my_index")
retriever = vector_store.as_retriever(search_kwargs={"k":2})
retriever.invoke("What is data fudiciary?")