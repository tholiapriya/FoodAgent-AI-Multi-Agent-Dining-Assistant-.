import os
import pandas as pd
from langchain_core.documents import Document
from langchain_chroma import Chroma  # Updated import
from langchain_huggingface import HuggingFaceEmbeddings

DB_PATH = "vector_db"

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

if os.path.exists(DB_PATH):
    vectorstore = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )
else:
    df = pd.read_csv("zomato.csv", encoding="latin1")
    documents = []
    for _, row in df.iterrows():
        text = f"Restaurant: {row['Restaurant Name']}\nCity: {row['City']}\nCuisine: {row['Cuisines']}\nRating: {row['Aggregate rating']}\nCost for two: {row['Average Cost for two']}\n"
        documents.append(Document(page_content=text))

    vectorstore = Chroma.from_documents(
        documents,
        embedding,
        persist_directory=DB_PATH
    )

retriever = vectorstore.as_retriever()