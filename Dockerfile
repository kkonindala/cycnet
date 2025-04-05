# Use a lightweight Python image
FROM python:3.7-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies and download model
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --default-timeout=600 -r requirements.txt

# Download the model from Google Drive
RUN pip install gdown && gdown --id 1fxlJsdv5ncJsdfv4in6YYxKgjIodmWdq -O /app/Model.h5

# Set the default port for Cloud Run
ENV PORT 8080

# Expose the port (optional, for local Docker - will be $PORT)
EXPOSE $PORT

# Start the Flask app with Gunicorn, using the PORT environment variable
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:$PORT", "app:app"]