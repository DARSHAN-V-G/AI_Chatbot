import pdfplumber

def extract_entire_pdf(pdf_path, txt_output_path):
    extracted_text = ""

    with pdfplumber.open(pdf_path) as pdf:
       
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n" 

    with open(txt_output_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(extracted_text)

pdf_path = r'E:\Repositories\AI_Chatbot\AI_Chatbot\src\AnatomyAndPhysiology.pdf'  
txt_output_path = r'E:\Repositories\AI_Chatbot\AI_Chatbot\src\extracted_text.txt'  

extract_entire_pdf(pdf_path, txt_output_path)

print(f"Entire PDF text extracted and saved to {txt_output_path}")
