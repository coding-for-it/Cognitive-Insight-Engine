# Financial Insight Analyzer

An AI-powered document analysis tool that extracts key performance indicators (KPIs) and sentiment from PDF or Excel-based annual reports. Designed to help analysts, consultants, and decision-makers quickly understand business documents.

## Features

- Upload support for **PDF** and **Excel (.xlsx)**
- Extracts **financial KPIs** like Revenue, Net Profit, and Profit Margin
- Performs **sentiment analysis** to detect overall tone (positive, neutral, negative)
- Detects important sections like "Financial Overview", "Management Discussion", etc.
- Built using **FastAPI (backend)** and **Streamlit (frontend)**

## Tech Stack

Layer       Technology             
Frontend    Streamlit               
Backend     FastAPI                 
NLP         TextBlob, Regex         
Parsing     pdfplumber, pandas      
File Types  PDF, Excel (.xlsx)      

