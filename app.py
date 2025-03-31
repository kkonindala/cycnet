import os
from flask import Flask, request, render_template, send_from_directory
import tensorflow as tf
import numpy as np
from PIL import Image
import keras
import gdown

# Print versions for debugging
print(keras.__version__)
print(tf.__version__)

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
'''file_id = "1fxlJsdv5ncJsdfv4in6YYxKgjIodmWdq"
download_url = f"https://drive.google.com/uc?id={"1fxlJsdv5ncJsdfv4in6YYxKgjIodmWdq"}"'''
model_path = "./Model.h5"

'''if not os.path.exists(model_path):
    gdown.download(download_url, model_path, quiet=False)'''

# Load the model with custom objects if needed
model = tf.keras.models.load_model(model_path)

# Define the path for saving uploaded images
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load and preprocess the input image
def preprocess_image(image_path, target_size):
    img = Image.open(image_path).convert("RGB")  # Open image and convert to RGB
    img = img.resize(target_size)                # Resize to match model input size
    img_array = np.array(img) / 255.0            # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['image']
        
        if file:
            # Save the uploaded file to the server
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Preprocess the image
            target_size = (512, 512)  # Model input size
            input_image = preprocess_image(filepath, target_size)

            # Make a prediction
            prediction = model.predict(input_image, verbose=1).round(2)
            cyclone_effect_percentage = prediction[0][0]  # Confidence for class 0 as percentage

            # Render the result page with image and prediction
            return render_template('result.html', image_file=file.filename, cyclone_effect_percentage=cyclone_effect_percentage)

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway assigns a PORT environment variable
    app.run(debug=True, host="0.0.0.0", port=port)
