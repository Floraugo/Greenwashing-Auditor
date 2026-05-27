# import fitz
# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = ""
#     for page in doc:
#       text += page.get_text()
#     return text
# sustainability_text = extract_text_from_pdf("report.pdf")
# print(sustainability_text[:500])

# import fitz

# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     # We will return a list of dictionaries with text and page numbers
#     extracted_data = []
    
#     for page_num, page in enumerate(doc, start=1):
#         text = page.get_text()
#         extracted_data.append({
#             "text": text,
#             "page": page_num
#         })
#     return extracted_data

# # Use the function
# # data = extract_text_from_pdf("report.pdf")
# data = extract_text_from_pdf("data/sustainability-statement-2024.pdf")

# # printing the page number for any chunk
# for item in data:
#     print(f"Evidence found on page: {item['page']}")
#     print(item['text'][:100]) # Print a preview

import fitz
import os  

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    extracted_data = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        extracted_data.append({"text": text, "page": page_num})
    return extracted_data

# 2. Define your folder
folder_path = "data"

# 3. Creating loop
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        full_path = os.path.join(folder_path, filename)
        print(f"--- Processing: {filename} ---")
        
        # Run your extraction
        data = extract_text_from_pdf(full_path)
        
        
        print(f"Successfully extracted {len(data)} pages from {filename}")