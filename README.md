# DOCX Recovery Script

This Python script attempts to recover text from corrupted DOCX files by extracting the content directly from the XML files inside the DOCX archive. It prompts the user for the DOCX file path, making it flexible and easy to use.

## Features
- Extracts text from `document.xml` and other XML files within a DOCX file.
- Bypasses XML structure errors to recover text content.
- Outputs recovered text to `recovered_text.txt`.

## Prerequisites

- Python 3.x
- `python-docx` library

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/AdnanTemur/repair-docx.git
    cd repair-docx
    ```

2. Install the required `python-docx` library:
    ```bash
    pip install python-docx
    ```

## Usage

1. Run the script:
    ```bash
    python repair-docx.py
    ```
2. When prompted, enter the path to the DOCX file you want to recover (e.g., `your_corrupted_file.docx`).
3. The recovered text will be saved to `recovered_text.txt`.

## Example

```bash
python repair-docx.py
Enter the path to the DOCX file you want to recover: your_corrupted_file.docx
Text has been extracted to recovered_text.txt
