import zipfile
import re

def extract_text_from_xml(xml_content):
    """Extract text from XML content by removing all tags."""
    text = re.sub(r'<[^>]+>', '', xml_content)  # Remove all XML tags
    return text

def extract_text_from_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            # Extract text from document.xml
            if 'word/document.xml' in zip_ref.namelist():
                document_xml = zip_ref.read('word/document.xml').decode('utf-8', errors='ignore')
                document_text = extract_text_from_xml(document_xml)
                print("Document text extracted.")
            else:
                print("No main document.xml found.")
                document_text = ""

            # Extract text from other parts if available
            other_text = []
            for item in zip_ref.namelist():
                if item.startswith('word/') and item.endswith('.xml') and item != 'word/document.xml':
                    xml_content = zip_ref.read(item).decode('utf-8', errors='ignore')
                    other_text.append(extract_text_from_xml(xml_content))

            full_text = document_text + '\n'.join(other_text)

            with open('recovered_text.txt', 'w', encoding='utf-8') as text_file:
                text_file.write(full_text)
            
            print("Text has been extracted to recovered_text.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user for the DOCX file name
    docx_file = input("Enter the path to the DOCX file you want to recover: ")
    extract_text_from_docx(docx_file)
