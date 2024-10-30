
# 🚀SmartCon Space and Time Hackathon Dashboard Complement using GenAI, Space and Time API, Google Docs API

## Overview
This project provides a dynamic dashboard and interactive tool for analyzing and visualizing an Ethereum dataset as part of a hackathon competition. Combining Space and Time SQL queries, Firebase storage for real-time image management, and a Google Docs integration, the project enables insightful and creative exploration of Ethereum data. This README offers detailed setup and usage instructions to facilitate seamless deployment and interaction with the tool.

## Table of Contents
1. [About the Project](#about-the-project)
2. [Technologies](#technologies)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Features](#features)
6. [Future Development](#future-development)
7. [Contributing](#contributing)

## About the Project
My Dashboard aims to stand out in the hackathon by using unique a storytelling theme: Biological evolution.

## The main feature
Dynamically creating markdowns based on the graph/data.
For example, my markdown is outdated a month later if the graph shows the data in the last 30 days. To fix that and keep markdowns automatically up-to-date.

## Workflow
Once in 10 days, the project will:
1. Run 10 SQL queries into the Space and Time Database API,
2. Resend the data with prompt to Poe API to generate markdowns,
3. Create word documents based on the generated markdowns,
4. Download the documents as PDF files and convert them into PNG files,
5. Upload the images to the Firebase,
6. Uploaded images are stored in the Firebase Storage and based on the link to the images, they will keep up-to-date,
7. Markdowns in the Dashboard are kept up-to-date since they use links to the images stored in the Firebase Storage.

## Technologies
This project utilizes:
- **Space and Time SQL API** for efficient data querying
- **AsyncPoeAPI** for natural language processing and prompt interaction
- **Firebase** for storing and managing images in real-time
- **Google Docs API** for creating and formatting documents
- **Aiogram** for Telegram bot functionalities and user interaction

## Setup
### Requirements
- Python 3.8+
- Necessary API keys (as listed below)

### Installation
1. Clone the repository:
    ```bash
    git clone [URL]
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the root directory and add the following keys:
    ```plaintext
    SPACE_AND_TIME_API_KEY=YOUR_KEY_HERE
    POE_P_B=YOUR_POE_P_B
    POE_P_LAT=YOUR_POE_P_LAT
    IMG1_ID=YOUR_IMG1_ID
    GOOGLE_DOCS_API_KEYNAME=YOUR_GOOGLE_DOCS_API_KEYNAME
    FIREBASE_API_KEYNAME=YOUR_FIREBASE_API_KEYNAME
    FIREBASE_STORAGE_BUCKET_NAME=YOUR_FIREBASE_BUCKET_NAME
    TELEGRAM_API=YOUR_TELEGRAM_API_KEY
    ```
4. Initialize Firebase and Google Docs by following their respective setup guides.

## Usage
1. **Data Query**:
   - Run the `query_space_and_time.py` script to fetch data from the Ethereum dataset using Space and Time SQL API.
2. **Image Management**:
   - Use `firebase_image_upload.py` to upload images to Firebase. This script follows a specific naming convention (e.g., `IMG_1.png`) and ensures images are updated in place.
3. **Google Docs Integration**:
   - Execute `google_docs_formatting.py` to update Google Docs with formatted content, images, and subsequently convert them to PDFs.
   - Additionally, use the script to download PDFs and convert them to images for further processing.
4. **Telegram Bot**:
   - Interact with the project data and images through the Aiogram bot. Supported commands include:
     - `send photo/file` — it will automatically upload to the firebase which will be up-to-date in the test dashboard's markdown
     - You can try it out at Telegram: @smartcon_test_bot


## Features
- **Data Exploration**: Advanced querying and analysis of the Ethereum dataset, allowing for insights and trend identification.
- **Real-Time Image Storage**: Firebase handles images, supporting auto-updates and consistent naming conventions.
- **Document Generation and Formatting**: Google Docs integration formats content, incorporates images, and exports documents as PDFs.
- **Interactive Telegram Bot**: Aiogram bot facilitates command-driven interactions, extending data access and updates to users.

## Future Development
- **Enhanced Visualizations**: Plan to integrate additional data visualizations and graphical analysis tools.
- **Advanced Analytics**: Develop further analytics functionalities using Space and Time data for richer insights.
- **Expanded Bot Commands**: Add more user-centric commands to the bot, enabling in-depth data exploration directly from Telegram.

## Contributing
We welcome contributions! If you'd like to help improve the project:
1. Fork the repository
2. Create a branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add a new feature'`)
4. Push to your branch (`git push origin feature/YourFeature`)
5. Open a Pull Request
