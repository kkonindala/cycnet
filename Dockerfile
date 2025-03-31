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
# Expose the port Flask runs on
EXPOSE 5000

# Start the Flask app with Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
