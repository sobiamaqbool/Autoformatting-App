## Autoformatting App

This project is a Flask web application that allows users to:
Upload PDF files and extract their text content.
Upload DOCX files and reformat them into a new document with custom styles (font, size, line spacing).
Generate a Table of Contents based on document headings.
Download the processed document.

## Features

# PDF Text Extraction:
Extract text from uploaded PDF files.
# DOCX Reformatting:
Customize fonts, sizes, line spacing for uploaded Word documents.
# Dynamic TOC Generation:
Automatically detect headings and generate a table of contents.
# Footer Page Numbering: 
Adds right-aligned page numbers to the footer.
# User Interface: 
Upload and configure document options via a simple HTML form.

## How It Works

# PDF Text Extraction
Users upload a PDF.
The app reads and extracts text from all pages.
The result is displayed or processed further.

# DOCX Reformatting
1. Users upload a .docx file.
2. The system detects headings and paragraphs.
3. The user selects:
    Font style (e.g., Times New Roman, Arial)
    Font size (e.g., 12, 14)
    Line spacing (e.g., 1.0, 1.5)
The app applies formatting, generates a Table of Contents, and allows users to download the result.

# Running the App
Ensure you have all dependencies installed.
Make sure uploads/ and templates/ folders exist.
Start the server:
Open your browser and go to: http://127.0.0.1:5000/

# Endpoints

/ or /home: Upload and select formatting options.
/upload: Handle file uploads and processing.
/about: Info page.
/contactus: Contact page.
/template: Example template page.
