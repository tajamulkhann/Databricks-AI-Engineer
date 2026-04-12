%pip install -U --quiet databricks-sdk==0.49.0 "databricks-langchain>=0.4.0" databricks-agents mlflow[databricks] databricks-vectorsearch==0.55 langchain==0.3.25 langchain_core==0.3.59 bs4==0.0.2 markdownify==0.14.1 pydantic==2.10.1 mlflow openai PyMuPDF

dbutils.library.restartPython()

from databricks_langchain import ChatDatabricks

chat_model = ChatDatabricks(
    endpoint="databricks-meta-llama-3-3-70b-instruct",
    temperature=0.1,
    max_tokens=250,
)

chat_model.invoke("Who is data fudiciary?")