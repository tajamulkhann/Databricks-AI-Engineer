# Our foundation model answering the final prompt
model =chat_model

#Let's try our prompt:
answer = (prompt | model | StrOutputParser()).invoke({'question':'Who is data fudiciary?', 'context': relevant_docs})

