from pypdf import PdfReader


def extract_resume_text(file_path):
    """
    Extract text from a PDF resume.
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def save_extracted_text(text, output_file):
    """
    Save extracted resume text for future AI processing.
    """

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)


if __name__ == "__main__":

    resume_path = "documents/resume/sample_resume.pdf"
    output_path = "data/resume_text.txt"

    resume_text = extract_resume_text(resume_path)

    save_extracted_text(resume_text, output_path)

    print("Resume extraction complete.")
    print(f"Extracted characters: {len(resume_text)}")
    print(f"Saved to: {output_path}")