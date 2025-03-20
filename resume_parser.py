import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extract text from a given PDF file."""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None
    
#Example Usage
if __name__ == "__main__":
    pdf_path = "sample_resume.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)