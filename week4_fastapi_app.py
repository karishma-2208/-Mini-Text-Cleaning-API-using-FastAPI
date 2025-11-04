from fastapi import FastAPI
from pydantic import BaseModel
import re
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords once
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Initialize FastAPI app
app = FastAPI(
    title="Mini Text Cleaning API",
    description="A simple FastAPI app that cleans text by removing punctuation, stopwords, and converting to lowercase.",
    version="1.0"
)

# Define input model
class TextInput(BaseModel):
    text: str

# Cleaning function
def clean_text(text):
    text = text.lower()  # lowercase
    text = re.sub(f"[{string.punctuation}]", "", text)  # remove punctuation
    tokens = text.split()  # tokenize
    tokens = [word for word in tokens if word not in stop_words]  # remove stopwords
    return " ".join(tokens)

# Route 1: Home
@app.get("/")
def home():
    return {"message": "Welcome to the Mini Text Cleaning API! Send a POST request to /clean_text"}

# Route 2: Clean text
@app.post("/clean_text")
def clean_endpoint(input_data: TextInput):
    cleaned = clean_text(input_data.text)
    return {"original_text": input_data.text, "cleaned_text": cleaned}
