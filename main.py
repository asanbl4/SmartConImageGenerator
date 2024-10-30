from update_content import update_document_content, upload_image_to_firebase
from file_converter import convert_pdf_to_jpg
from downloader import download_doc_as_pdf
from spaceandtime import send_sql
from poe import send_prompt


async def fetch_sql_data(query):
    # Wrapping send_sql in an async function to await its result
    return send_sql(query)


async def main(query, example):
    result_of_sql = await fetch_sql_data(query)
    print(result_of_sql)
    await send_prompt(example + result_of_sql)


if __name__ == '__main__':
    for i in range(1, 11):
        if_dark = True
        if not i % 2:
            if_dark = False
        header_text = ""
        body_text = ""
        doc_id = update_document_content(i, if_dark)
        download_doc_as_pdf(doc_id=doc_id, output_path=f"IMG{i}.pdf")
        convert_pdf_to_jpg(f"IMG{i}.pdf", f"IMG{i}.png")
        firebase_url = upload_image_to_firebase(f"IMG{i}.png")