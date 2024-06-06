# This code convert the images with text to text format. 

import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use Tesseract to extract text
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Specify the path to the image file
    image_path = "plate.jpg"
    
    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)
    
    # Print the extracted text
    print("Extracted Text:" + extracted_text)
