#!/usr/bin/env python3
import PyPDF2
import os

pdf_path = r'c:\Users\mniedziolka\Downloads\LLMAll_en-US_FINAL.pdf'
output_path = r'c:\Users\mniedziolka\Downloads\pdf_extracted.txt'

# Check if PDF exists
if not os.path.exists(pdf_path):
    with open(output_path, 'w') as f:
        f.write(f"ERROR: PDF file not found at {pdf_path}")
    exit(1)

# Extract text
try:
    with open(pdf_path, 'rb') as pdffile:
        reader = PyPDF2.PdfReader(pdffile)
        num_pages = len(reader.pages)
        
        all_text = f"PDF Extraction Report\n" \
                   f"====================\n" \
                   f"File: {pdf_path}\n" \
                   f"Total Pages: {num_pages}\n" \
                   f"\n{'='*80}\n\n"
        
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            all_text += f"\n--- Page {page_num + 1} ---\n"
            all_text += page_text + "\n"
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(all_text)
    
    # Also print confirmation
    with open(output_path + '.status', 'w') as f:
        f.write(f"SUCCESS: Extracted {num_pages} pages\n")
        
except Exception as e:
    with open(output_path, 'w') as f:
        f.write(f"ERROR: {str(e)}\n")
        import traceback
        f.write(traceback.format_exc())
