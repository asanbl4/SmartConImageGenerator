from googleapiclient.http import MediaFileUpload
from auth import service, drive_service  # Connect Google Docs and Drive API clients
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

# Specify the document ID (from the Google Docs URL)
DOCUMENT_ID = os.getenv('IMG1_ID')
IMAGE_PATH = 'testimg.jpeg'  # Path to the image


def upload_image_to_drive(image_path):
    # Upload image to Google Drive
    file_metadata = {'name': 'Test Image', 'mimeType': 'image/jpeg'}
    media = MediaFileUpload(image_path, mimetype='image/jpeg')

    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    file_id = uploaded_file.get('id')

    # Make the image publicly accessible
    drive_service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()

    print(f"Image uploaded and made public successfully with ID: {file_id}")
    with open('data.json', 'w') as file:
        json.dump({"footer": file_id}, file)

    return file_id


def update_document_content():
    # Clear existing content in the document
    doc = service.documents().get(documentId=DOCUMENT_ID).execute()
    content_length = doc.get('body').get('content')[-1].get('endIndex') - 1

    clear_request = [
        {
            'deleteContentRange': {
                'range': {
                    'startIndex': 1,
                    'endIndex': content_length
                }
            }
        }
    ]

    service.documents().batchUpdate(
        documentId=DOCUMENT_ID, body={'requests': clear_request}).execute()

    # Define the text and line breaks before the image
    text_content = "First line of text.\nSecond line of text.\nThird line of text."
    additional_line_breaks = "\n" * (6 - text_content.count('\n'))  # Two line breaks after the text

    # Insert the text and line breaks at the beginning of the document
    new_content_request = [
        {
            'insertText': {
                'location': {'index': 1},
                'text': text_content + additional_line_breaks
            }
        }
    ]

    service.documents().batchUpdate(
        documentId=DOCUMENT_ID, body={'requests': new_content_request}).execute()

    print("New content with custom text and line breaks inserted successfully!")
    time.sleep(5)

    # Upload the image if it hasn't been uploaded yet
    with open("data.json", "r") as file:
        data = json.load(file)

    image_file_id = data['footer'] if data['footer'] else upload_image_to_drive(IMAGE_PATH)

    # Insert the image at the appropriate index (after text and line breaks)
    image_index = len(text_content) + len(additional_line_breaks)

    insert_image_request = [
        {
            'insertInlineImage': {
                'location': {'index': image_index},
                'uri': f'https://drive.google.com/uc?export=view&id={image_file_id}',
                'objectSize': {
                    'height': {'magnitude': 200, 'unit': 'PT'},
                    'width': {'magnitude': 200, 'unit': 'PT'}
                }
            }
        }
    ]

    service.documents().batchUpdate(
        documentId=DOCUMENT_ID, body={'requests': insert_image_request}).execute()

    print("Image inserted successfully after text and line breaks!")
    return DOCUMENT_ID


# Run the document update function
if __name__ == '__main__':
    update_document_content()
