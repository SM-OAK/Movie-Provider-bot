# We use bullseye-slim because the old buster repositories are dead
FROM python:3.10-slim-bullseye

# Install system dependencies for Pillow, OpenCV, and Git
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your bot code
COPY . .

# Start the bot
CMD ["python3", "bot.py"]

