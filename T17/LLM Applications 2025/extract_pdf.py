import PyPDF2
import sys

pdf_path = r'c:\Users\mniedziolka\Downloads\LLMAll_en-US_FINAL.pdf'

try:
    print(f'Opening PDF: {pdf_path}', file=sys.stderr)
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)
        print(f'Total pages: {total_pages}')
        
        text = ''
        for i, page in enumerate(reader.pages):
            page_text = f'\n--- Page {i+1} ---\n'
            page_text += page.extract_text()
            text += page_text
            if (i + 1) % 10 == 0:
                print(f'Processed {i+1} pages...', file=sys.stderr)
        
        print(f'Total extracted text length: {len(text)} characters')
        # Write to a temporary file for reading
        output_file = r'c:\Users\mniedziolka\Downloads\pdf_content.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'PDF content extracted successfully to {output_file}')
except Exception as e:
    import traceback
    print(f'Error: {e}', file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
