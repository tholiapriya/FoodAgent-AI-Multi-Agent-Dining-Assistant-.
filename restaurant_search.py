from rag_system import retriever

def get_restaurant_context(query):
    # .invoke() is the modern LangChain standard
    docs = retriever.invoke(query)

    context = ""
    for doc in docs[:3]:
        context += doc.page_content + "\n"

    return context