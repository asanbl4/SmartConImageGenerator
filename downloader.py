from auth import drive_service


def download_doc_as_pdf(doc_id, output_path):
    request = drive_service.files().export(fileId=doc_id, mimeType='application/pdf')
    pdf_data = request.execute()

    with open(output_path, 'wb') as pdf_file:
        pdf_file.write(pdf_data)

    print(f"Document downloaded as PDF at {output_path}")