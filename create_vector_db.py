from langchain_text_splitters import RecursiveCharacterTextSplitter

# Read Corpus
with open("rbi_corpus.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(text)

print("Total Chunks:", len(chunks))

# Save chunks for verification
with open("chunks.txt", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        f.write(f"\n\n----- CHUNK {i+1} -----\n")
        f.write(chunk)

print("Chunks saved successfully")