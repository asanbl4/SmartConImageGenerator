from update_content import update_document_content
from file_converter import convert_pdf_to_jpg
from downloader import download_doc_as_pdf


if __name__ == '__main__':
    doc_id = update_document_content()
    download_doc_as_pdf(doc_id=doc_id, output_path="IMG1.pdf")
    convert_pdf_to_jpg("IMG1.pdf", "IMG1.jpeg")