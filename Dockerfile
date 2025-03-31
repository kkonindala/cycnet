# Use Python 3.7 image
FROM python:3.7

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (or the port your app runs on)
EXPOSE 5000

# Run Flask app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
