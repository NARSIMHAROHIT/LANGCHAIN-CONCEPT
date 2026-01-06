from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import PyPDFLoader

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read dataset path from .env
data_path = os.getenv("DATA_PATH")

if not data_path:
    raise ValueError("DATA_PATH not found in .env file")

documents = []
#================{CSV Loader} ================
# Load all CSV files in the dataset directory
for file in os.listdir(data_path):
    if file.endswith(".csv"):
        file_path = os.path.join(data_path, file)
        loader = CSVLoader(file_path=file_path)
        documents.extend(loader.load())

print(f"Loaded {len(documents)} documents")

#============== {PDF LAODER}==================
loader = PyPDFLoader("data/Python_codeslearning.pdf")

docs = loader.load()

print(f"Documents loaded successfully: {len(docs)}")
print(docs[:10])
