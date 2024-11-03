# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies needed for package compilation
RUN apt-get update && apt-get install -y \
    gcc \
    libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the bot's source code
COPY . .

# Run the bot
CMD ["python", "bot.py"]
