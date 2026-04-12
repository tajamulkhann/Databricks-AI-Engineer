spark_df = spark.createDataFrame(pd_docs[['id_pk','page_content']])
spark_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable("workspace.default.my_data_chuks")