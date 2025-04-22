import json
from sentence_transformers import SentenceTransformer

# Load the mock threads
with open('mock_threads.json', 'r') as f:
    threads = json.load(f)

# Loading a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings
for thread in threads:
    embedding = model.encode(thread['content'])
    thread['embedding'] = embedding.tolist()

# Save the results
with open('embedded_threads.json', 'w') as f:
    json.dump(threads, f, indent=2)

print("Embeddings generated and saved to embedded_threads.json")
