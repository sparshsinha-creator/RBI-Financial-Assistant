# RBI Financial Intelligence Platform

AI-powered Financial Intelligence Platform that analyzes RBI reports, monetary policy documents, financial stability reports, and macroeconomic datasets using Retrieval-Augmented Generation (RAG), semantic search, and vector databases.

## Data Sources

### RBI Reports

* annual_report_2025_26.pdf
* financial_stability_report.pdf
* monetary_policy_report.pdf

### Economic Datasets

* rbi_inflation_money_credit_indicators.xlsx
* rbi_macroeconomic_indicators.xlsx

## Features

* PDF & Excel Data Ingestion
* Automated Text Extraction
* Text Chunking & Processing
* Semantic Search using FAISS
* Financial Question Answering
* RBI Report Analysis
* Streamlit-based Interactive Interface

## Tech Stack

* Python
* Streamlit
* FAISS
* Sentence Transformers
* Pandas
* PyPDF
* NumPy
* NLP

## Architecture

RBI Reports (PDF/Excel)
→ Data Ingestion
→ Text Extraction
→ Chunking
→ Embeddings Generation
→ FAISS Vector Database
→ Semantic Search
→ Financial Intelligence Assistant

## Sample Questions

* What is RBI's inflation outlook?
* Explain the inflation targeting framework.
* What are the key highlights of the Financial Stability Report?
* Explain the current monetary policy stance.
* What are the major macroeconomic risks highlighted by RBI?
* What is the trend in bank credit growth?
* Explain the role of the Monetary Policy Committee (MPC).

## Project Structure

```text
RBI-Financial-Assistant/
│
├── app.py
├── ingest.py
├── create_vector_db.py
├── build_vector_db.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── annual_report_2025_26.pdf
│   ├── financial_stability_report.pdf
│   ├── monetary_policy_report.pdf
│   ├── rbi_inflation_money_credit_indicators.xlsx
│   └── rbi_macroeconomic_indicators.xlsx
│
├── rbi_vector.index
└── rbi_chunks.pkl
```

## Author

**Sparsh Sinha**

GitHub: https://github.com/sparshsinha-creator

