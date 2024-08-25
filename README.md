# DOCX Recovery Script

This Python script attempts to recover text from corrupted DOCX files by extracting the content directly from the XML files inside the DOCX archive. It prompts the user for the DOCX file path, making it flexible and easy to use.

## Features
- Extracts text from `document.xml` and other XML files within a DOCX file.
- Bypasses XML structure errors to recover text content.
- Outputs recovered text to `recovered_text.txt`.

## Prerequisites

- Python 3.x
- No external libraries required (uses Python's standard library).

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/docx-recovery-script.git
    cd docx-recovery-script
    ```

## Usage

1. Run the script:
    ```bash
    python extract_docx_text.py
    ```
2. When prompted, enter the path to the DOCX file you want to recover (e.g., `your_corrupted_file.docx`).
3. The recovered text will be saved to `recovered_text.txt`.

## Example

```bash
Enter the path to the DOCX file you want to recover: your_corrupted_file.docx
Text has been extracted to recovered_text.txt
