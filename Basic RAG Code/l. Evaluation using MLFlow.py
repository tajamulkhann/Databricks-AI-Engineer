'''Evaluating a **RAG (Retrieval-Augmented Generation)** application is more complex than standard ML because you have to measure two distinct things: how well you **retrieved** information and how well you **generated** the final answer.

[MLflow](https://mlflow.org/llm-evaluation) categorizes these into **Heuristic (Code-based)** and **LLM-as-a-Judge** metrics.

### **1. The "RAG Triad" (Quality Metrics)**

These are typically handled by "LLM-as-a-Judge," where a stronger model (like GPT-4) evaluates your RAG pipeline's output.

  * **Faithfulness / Groundedness:** Measures if the answer is derived *only* from the retrieved context. This is the primary check for hallucinations.
  * **Answer Relevance:** Measures how well the final response addresses the user's initial query, regardless of the context.
  * **Context Relevance / Retrieval Sufficiency:** Measures if the retrieved documents actually contain the information needed to answer the question.

### **2. Retrieval Performance Metrics**

If you have "ground truth" (the exact document IDs that *should* have been found), [MLflow](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.metrics.html) can track:

  * **Precision@k:** How many of the top *k* retrieved documents were actually relevant?
  * **Recall@k:** Did the retriever find all the relevant documents within the top *k* results?
  * **nDCG (Normalized Discounted Cumulative Gain):** Does the retriever put the *most* relevant documents at the very top of the list?

### **3. Content Generation Metrics**

These focus on the linguistic quality of the LLM's response:

  * **Perplexity:** A measure of how "certain" the model is. Lower perplexity usually means more coherent, predictable text.
  * **Toxicity:** Flags harmful, biased, or inappropriate content.
  * **Readability (ARI/Flesch-Kincaid):** Tracks the complexity of the output (e.g., is it written at a 5th-grade level or a PhD level?).
  * **ROUGE / BLEU:** Traditional metrics that measure word-overlap between the generated answer and a reference "perfect" answer.

### **4. Operational & Cost Metrics**

MLflow [Tracing](https://www.google.com/search?q=https://mlflow.org/cookbook/rag-evaluation) automatically captures the "plumbing" of your app:

  * **Latency:** How long each step takes (Retrieval vs. Generation).
  * **Token Usage:** Tracking `prompt_tokens` and `completion_tokens` to monitor costs.
  * **Tool Call Efficiency:** For agentic RAG, it tracks if the model is calling the right tools in a logical order without getting stuck in loops.

-----

### **Quick Comparison Table**

| Metric Type | Example Metric | Best For... |
| :--- | :--- | :--- |
| **Retrieval** | Recall@k, nDCG | Testing your Vector DB/Search quality. |
| **Generation** | Faithfulness, Toxicity | Ensuring the AI doesn't hallucinate or offend. |
| **End-to-End** | Answer Relevance | Checking if the user actually gets what they asked for. |
| **Operations** | Latency, Token Count | Managing production costs and speed. |

'''

mlflow.evaluate(
    model, 
    data, 
    evaluators=["question-answering"]
)