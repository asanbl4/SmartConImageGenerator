from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials

load_dotenv()

# Provide the path to your service account JSON key
SERVICE_ACCOUNT_FILE = os.getenv('GOOGLE_DOCS_API_KEYNAME')

# Define the required scopes
SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive'
]

# Authenticate the service account
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Google Docs service
service = build('docs', 'v1', credentials=creds)

# Build the Google Drive service
drive_service = build('drive', 'v3', credentials=creds)

# Firebase setup
cred = credentials.Certificate(os.getenv("FIREBASE_API_KEYNAME"))  # Replace with your Firebase JSON key path
firebase_admin.initialize_app(cred, {
    'storageBucket': os.getenv("FIREBASE_STORAGE_BUCKET_NAME")})  # Replace with your bucket name
