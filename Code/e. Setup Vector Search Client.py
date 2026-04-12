from databricks.vector_search.client import VectorSearchClient
client = VectorSearchClient()
index=client.get_index(index_name="workspace.default.my_index")
 
results_dict=index.similarity_search(
     query_text="Who is Data Fudiciary?",
     columns=["id_pk", "page_content"],
     num_results=2
 )
 
display(results_dict)