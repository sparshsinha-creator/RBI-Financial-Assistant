from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Read chunks
with open("chunks.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = text.split("----- CHUNK ")

print("Total Chunks:", len(chunks))

# Embedding Model
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

# FAISS Index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS DB
faiss.write_index(index, "rbi_vector.index")

# Save chunks
with open("rbi_chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Vector Database Created Successfully!")