FROM python:3.10-slim

# Install system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libboost-all-dev \
    python3-dev \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install face_recognition directly (includes dlib prebuilt)
RUN pip install --no-cache-dir face_recognition

# Install other dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "server.py"]
