from googleapiclient.http import MediaFileUpload
from auth import service, drive_service # Connect Google Docs and Drive API clients
from dotenv import load_dotenv
import os
import json
import time
from firebase_admin import storage

load_dotenv()


DOCUMENT_ID = os.getenv('IMG1_ID')
IMAGE_PATH = 'insert.jpeg'  # Path to the image


def upload_image_to_firebase(image_path="IMG1.png"):
    image_name = image_path
    bucket = storage.bucket()
    blob = bucket.blob(image_name)

    # Upload the image and override any existing file with the same name
    blob.upload_from_filename(image_path)

    # Set the image to be publicly accessible
    blob.make_public()

    print(f"Image uploaded to Firebase Storage with URL: {blob.public_url}")

    return blob.public_url


def upload_image_to_drive(image_path):
    file_metadata = {'name': 'Test Image', 'mimeType': 'image/png'}
    media = MediaFileUpload(image_path, mimetype='image/png')

    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    file_id = uploaded_file.get('id')

    drive_service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()

    print(f"Image uploaded and made public successfully with ID: {file_id}")
    with open('data.json', 'w') as file:
        json.dump({"footer": file_id}, file)

    return file_id


def update_document_content():
    doc = service.documents().get(documentId=DOCUMENT_ID).execute()
    content_length = doc.get('body').get('content')[-1].get('endIndex') - 1

    # Clear previous content
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

    # Define header and body texts
    header_text = "First Movement: Daily Transactions Crescendo"
    body_text = (
        "Watch as the daily transactions soar, painting a vivid picture of zkSync's growingd. adoption. "
        "This rising melody represents more users discovering the power and efficiency of layer-2 scaling."
    )
    additional_line_breaks = "\n" * 2

    # Format header text
    header_request = [
        {
            'insertText': {
                'location': {'index': 1},
                'text': header_text + "\n\n"
            }
        },
        {
            'updateTextStyle': {
                'range': {
                    'startIndex': 1,
                    'endIndex': len(header_text) + 1,
                },
                'textStyle': {
                    'bold': True,
                },
                'fields': 'bold'
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 1,
                    'endIndex': len(header_text) + 1,
                },
                'fields': 'alignment'
            }
        }
    ]

    body_request = [
        {
            'insertText': {
                'location': {'index': len(header_text) + 3},
                'text': body_text + additional_line_breaks
            }
        },
        {
            'updateTextStyle': {
                'range': {
                    'startIndex': len(header_text) + 3,
                    'endIndex': len(header_text) + 3 + len(body_text),
                },
                'textStyle': {
                    'weightedFontFamily': {
                        'fontFamily': 'Poppins'
                    }
                },
                'fields': 'weightedFontFamily'
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': len(header_text) + 3,
                    'endIndex': len(header_text) + 3 + len(body_text),
                },
                'fields': 'alignment'
            }
        }
    ]

    service.documents().batchUpdate(
        documentId=DOCUMENT_ID, body={'requests': header_request + body_request}).execute()

    print("Document updated with formatted header and body text!")
    time.sleep(5)

    # Load image ID from data.json or upload a new image to Drive
    with open("data.json", "r") as file:
        data = json.load(file)

    image_file_id = data['footer'] if data['footer'] else upload_image_to_drive(IMAGE_PATH)

    # Calculate the image insertion index
    image_index = len(header_text) + len(body_text) + len(additional_line_breaks) + 3

    # Insert image
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

    print("Image inserted successfully after header and body text!")
    return DOCUMENT_ID


if __name__ == '__main__':
    update_document_content()
    firebase_url = upload_image_to_firebase("IMG1.png")  # Upload the image to Firebase
