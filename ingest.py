import os
import pandas as pd
from pypdf import PdfReader

# Data folder
DATA_FOLDER = "data"

# Saara text store hoga
all_text = ""

print("Reading files from data folder...\n")

for file in os.listdir(DATA_FOLDER):

    # Full file path
    file_path = os.path.join(DATA_FOLDER, file)

    # PDF Files
    if file.lower().endswith(".pdf"):

        print(f"Reading PDF: {file}")

        reader = PdfReader(file_path)

        for page in reader.pages:

            text = page.extract_text()

            if text:
                all_text += text + "\n"

    # Excel Files
    elif file.lower().endswith(".xlsx"):

        print(f"Reading Excel: {file}")

        df = pd.read_excel(file_path)

        all_text += df.to_string(index=False)
        all_text += "\n"

print("\n-----------------------------------")
print("Total Characters:", len(all_text))
print("-----------------------------------")

# Save combined corpus
with open("rbi_corpus.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("\nCorpus saved successfully!")
print("File Created: rbi_corpus.txt")