import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tensorflow as tf
print(tf.__version__)
model = tf.keras.models.load_model('./Model.h5')
# Load and preprocess the input image
def preprocess_image(image_path, target_size):
    img = Image.open(image_path).convert("RGB")  # Open image and convert to RGB
    img = img.resize(target_size)               # Resize to match model input size
    img_array = np.array(img) / 255.0           # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array
 
# Example: Single input image test
image_path = "test_image.png"  # Replace with your image path
target_size = (512, 512)  # Replace with your model's expected input size
input_image = preprocess_image(image_path, target_size=target_size)

# Test image with the model
prediction = model.predict(input_image, verbose=1).round(2) # Replace 'model' with your trained model  model.predict(train_data, verbose=1).round(2)
cyclone_effect_percentage = prediction[0][0] # Confidence for class 0 as percentage
print(cyclone_effect_percentage)

# Visualization
plt.figure(figsize=(5, 5))
plt.imshow(input_image[0])  # Remove batch dimension for display
plt.title(f"Cyclone Effect: {cyclone_effect_percentage:}knots")  # Display percentage in title
plt.axis("off")
plt.show()
