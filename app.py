from flask import Flask, request, render_template
import PyPDF2

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('upload.html', error='No file part')

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            return render_template('upload.html', error='No selected file')

        # If file is uploaded successfully, process and display text
        if file:
            text = extract_text_from_pdf(file)
            return render_template('show.html', text=text)

    return render_template('show.html')
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    return text
if __name__ == '__main__':
    app.run(debug=True)
