import os
from aiogram import Bot, Router, types
from aiogram import Dispatcher
from dotenv import load_dotenv
from firebase_admin import storage, initialize_app, credentials

# Load environment variables
load_dotenv()

# Initialize Firebase
cred = credentials.Certificate(os.getenv("FIREBASE_API_KEYNAME"))
initialize_app(cred, {'storageBucket': os.getenv("FIREBASE_STORAGE_BUCKET_NAME")})

# Initialize Bot and Dispatcher
API_TOKEN = os.getenv("TELEGRAM_API")
bot = Bot(token=API_TOKEN)
router = Router()


# Define handler to save and upload image
@router.message(lambda message: message.photo)
async def save_and_upload_image(message: types.Message):
    # Save the received image as 'testimg.png'
    photo = message.photo[-1]  # Gets the highest resolution photo
    file = await bot.get_file(photo.file_id)
    await bot.download_file(file.file_path, destination="testimg.png")

    # Upload image to Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob("testimg.png")
    blob.upload_from_filename("testimg.png")
    blob.make_public()

    await message.reply(f"Image saved and uploaded successfully! Firebase URL: {blob.public_url}")


# Set up dispatcher and polling
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
