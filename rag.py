import pandas as pd
import faiss
import numpy as np
import google.generativeai as genai
from sentence_transformers import SentenceTransformer

sbert_model = SentenceTransformer("all-MiniLM-L6-v2")

def load_cricket_data(csv_path):
    df = pd.read_csv(csv_path)
    df.fillna("", inplace=True)
    df["text"] = df.apply(lambda row: " ".join(row.astype(str)), axis=1)
    return df["text"].tolist()

def create_faiss_index(texts):
    embeddings = sbert_model.encode(texts, convert_to_numpy=True)
    d = embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(embeddings)
    return index, embeddings, texts

def search_faiss(index, query, texts, k=3):
    query_embedding = sbert_model.encode([query], convert_to_numpy=True)
    D, I = index.search(query_embedding, k)
    results = [texts[i] for i in I[0]]
    return results

genai.configure(api_key="YOUR_GEMINI_API_KEY")

def generate_response(query, retrieved_data):
    prompt = f"""
    You are a cricket expert. Answer the user's question based on the retrieved cricket data below:

    Retrieved Data:
    {retrieved_data}

    User Query:
    {query}

    Provide a detailed but concise response.
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text if response else "I couldn't generate a response."

def main():
    csv_path = "cricket_data.csv"
    texts = load_cricket_data(csv_path)
    index, embeddings, stored_texts = create_faiss_index(texts)

    while True:
        query = input("Ask a Cricket Question (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        retrieved_data = search_faiss(index, query, stored_texts, k=3)
        response = generate_response(query, "\n".join(retrieved_data))
        print("\nGemini's Response:")
        print(response)

if __name__ == "__main__":
    main()
