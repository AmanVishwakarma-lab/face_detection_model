# Use a base image with Python and system tools
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for dlib and face_recognition
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-python-dev \
    && apt-get clean

# Copy your application code
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask app (or your web server)
EXPOSE 5000

# Start your app
CMD ["python", "main.py"]
