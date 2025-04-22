import json
import numpy as np
import subprocess
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

with open('embedded_threads.json', 'r') as f:
    threads = json.load(f)

# Loading the sentence transformer
model = SentenceTransformer('all-MiniLM-L6-v2')

#Ollama explanation generator using LLaMA
def generate_explanation_ollama(query, content, model_name="llama2"):
    prompt = f"""
You are an assistant that helps explain search matches to users.
The user searched for: "{query}"
Here is a thread that was retrieved: "{content}"

Explain in 1–2 sentences why this thread is relevant to the query.
Avoid repeating the thread. Focus on *why it matched* semantically or thematically.
"""

    result = subprocess.run(
        ['ollama', 'run', model_name],
        input=prompt,
        text=True,
        stdout=subprocess.PIPE
    )
    return result.stdout.strip()

#Semantic search function
def search_threads(query, top_k=5):
    query_embedding = model.encode([query])

    thread_embeddings = np.array([t['embedding'] for t in threads])
    similarities = cosine_similarity(query_embedding, thread_embeddings)[0]

    # Rank threads by similarity
    ranked_indices = np.argsort(similarities)[::-1][:top_k]

    results = []
    for idx in ranked_indices:
        thread = threads[idx]
        explanation = generate_explanation_ollama(query, thread['content'])
        results.append({
            "id": thread['id'],
            "title": thread['title'],
            "content": thread['content'],
            "score": float(similarities[idx]),
            "why_this": explanation
        })

    return results

#Run from CLI
if __name__ == "__main__":
    user_query = input("Enter your thread query: ")
    matches = search_threads(user_query)

    print("\n🔍 Top Matches:")
    for match in matches:
        print(f"\n🧵 {match['title']} (Score: {match['score']:.4f})")
        print(f"{match['content']}")
        print(f"💡 Why this? {match['why_this']}")
