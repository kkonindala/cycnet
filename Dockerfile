# Use a lightweight Python image
FROM python:3.7-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

RUN pip install --upgrade pip setuptools wheel

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000
RUN pip install gdown && \
    gdown "https://drive.google.com/uc?id=1fxlJsdv5ncJsdfv4in6YYxKgjIodmWdq" -O /app/model.h5

# Start the Flask app with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
