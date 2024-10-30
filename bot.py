import os
from aiogram import Bot, Router, types
from aiogram import Dispatcher
from dotenv import load_dotenv
from update_content import upload_image_to_firebase

# Load environment variables
load_dotenv()

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
    upload_image_to_firebase("testimg.png")

    await message.reply(f"Image saved and uploaded successfully! Firebase URL: https://firebasestorage.googleapis.com/v0/b/smartconhackathon-6d75b.appspot.com/o/testimg.png?alt=media&token=d1e9e6a6-948d-40f7-b6ff-8a57186c0a9b")


@router.message(lambda message: message.document and message.document.mime_type.startswith("image/"))
async def save_and_upload_image_file(message: types.Message):
    # Save the received image as 'testimg.png'
    file = await bot.get_file(message.document.file_id)
    await bot.download_file(file.file_path, destination="testimg.png")

    # Upload image to Firebase Storage
    upload_image_to_firebase("testimg.png")

    await message.reply("Image saved and uploaded successfully! URL: https://firebasestorage.googleapis.com/v0/b/smartconhackathon-6d75b.appspot.com/o/testimg.png?alt=media&token=d1e9e6a6-948d-40f7-b6ff-8a57186c0a9b")

# Set up dispatcher and polling
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
