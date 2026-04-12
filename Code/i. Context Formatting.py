from databricks_langchain import DatabricksVectorSearch
vector_store = DatabricksVectorSearch(index_name="workspace.default.my_index")
retriever = vector_store.as_retriever(search_kwargs={"k":2})
relevant_documents=retriever.invoke("What is data fudiciary?")
relevant_documents

# Method to format the docs returned by the retriever into the prompt (keep only the text from chunks)
def format_context(docs):
    chunk_contents = [f"Passage: {d.page_content}\n" for d in docs]
    return "".join(chunk_contents)
format_context(relevant_documents)