# This code will convert the bulk images with text from a folder to the text format using "Detect Document Text API" of Amazon Textract. The data output is selected in Layout format.
# Pricing : $1.50 for first 1 million pages and $0.60 after 1 million pages. (1000 pages free for free tier account).

import boto3
import os
from PIL import Image

def extract_text_from_image(image_path):
    # Initialize Textract client
    textract = boto3.client('textract')

    # Read image file
    with open(image_path, 'rb') as document:
        imageBytes = document.read()

    # Call Textract
    response = textract.detect_document_text(Document={'Bytes': imageBytes})

    # Process response and collect detected text with at least 5 non-space characters
    detected_text = []
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            text = block['Text'].replace(' ', '')  # Remove spaces
            if len(text) >= 5:
                detected_text.append(block['Text'])

    # Join the detected text lines into a single string
    full_text = '\n'.join(detected_text)
    return full_text

def extract_text_from_folder(folder_path):
    # Supported image extensions
    supported_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']

    # List all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in supported_extensions]

    # Extract text from each image file
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        print(f"Extracting text from {image_file}...")
        try:
            extracted_text = extract_text_from_image(image_path)
            if extracted_text:
                print(f"Detected text:\n{extracted_text}\n")
            else:
                print("No text found or text is less than 5 characters.\n")
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

# Path to the folder containing images
folder_path = 'D:/vinimages'
extract_text_from_folder(folder_path)
