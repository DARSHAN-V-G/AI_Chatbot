import pdfplumber

def extract_entire_pdf(pdf_path, txt_output_path):
    extracted_text = ""

    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through all the pages
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"  # Add a newline after each page

    # Save the extracted text to a text file with UTF-8 encoding
    with open(txt_output_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(extracted_text)

# Define the paths
pdf_path = r'E:\Repositories\AI_Chatbot\AI_Chatbot\src\AnatomyAndPhysiology.pdf'  # Replace with your PDF file path
txt_output_path = r'E:\Repositories\AI_Chatbot\AI_Chatbot\src\extracted_text.txt'  # Replace with your desired output text file path

# Call the function to extract the entire PDF text and save it
extract_entire_pdf(pdf_path, txt_output_path)

print(f"Entire PDF text extracted and saved to {txt_output_path}")
