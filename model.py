from transformers import pipeline
from pydantic import BaseModel
from typing import List, Dict

# Load AI models for Named Entity Recognition (NER) and summarization
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER")
summarizer = pipeline("summarization")

class ResumeData(BaseModel):
    name: str
    email: str
    phone: str
    skills: List[str]
    experience: str
    education: str

def extract_entities(text: str) -> Dict[str, str]:
    """Extracts named entities like name, email, and phone using NLP."""
    entities = {"name": "", "email": "", "phone": ""}
    for entity in ner_pipeline(text):
        if entity['entity'] == 'B-PER':
            entities['name'] = entity['word']
        elif entity['entity'] == 'B-EMAIL':
            entities['email'] = entity['word']
        elif entity['entity'] == 'B-PHONE':
            entities['phone'] = entity['word']
    return entities

def extract_skills(text: str) -> List[str]:
    """Extracts skills from the resume text (can be improved with a custom model)."""
    skills = [word for word in text.split() if word.lower() in ["python", "ml", "ai", "tensorflow", "azure", "qdrant"]]
    return skills

def summarize_experience(text: str) -> str:
    """Summarizes work experience using AI."""
    return summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']

def parse_resume(text: str) -> ResumeData:
    """Parses a resume text and extracts structured information."""
    entities = extract_entities(text)
    skills = extract_skills(text)
    experience = summarize_experience(text)
    education = "Placeholder for education extraction logic"
    return ResumeData(
        name=entities['name'],
        email=entities['email'],
        phone=entities['phone'],
        skills=skills,
        experience=experience,
        education=education
    )
