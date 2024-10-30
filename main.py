from update_content import update_document_content, upload_image_to_firebase
from file_converter import convert_pdf_to_jpg
from downloader import download_doc_as_pdf


if __name__ == '__main__':
    for i in range(1, 3):
        if_dark = False
        if i == 2:
            if_dark = True
        doc_id = update_document_content(i, if_dark)
        download_doc_as_pdf(doc_id=doc_id, output_path=f"IMG{i}.pdf")
        convert_pdf_to_jpg(f"IMG{i}.pdf", f"IMG{i}.png")
        firebase_url = upload_image_to_firebase(f"IMG{i}.png")