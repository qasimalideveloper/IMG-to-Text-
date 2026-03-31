import cv2
import pytesseract
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

tesseract_path = os.path.join(current_dir, "Tesseract-OCR", "tesseract.exe")

pytesseract.pytesseract.tesseract_cmd = tesseract_path

def image_to_text(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding for better OCR accuracy
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(gray)
    
    return text

def process_images_in_folder(folder_path):
    output_folder = os.path.join(folder_path, "extracted_texts")
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            extracted_text = image_to_text(image_path)
            
            text_filename = os.path.splitext(filename)[0] + ".txt"
            text_filepath = os.path.join(output_folder, text_filename)
            
            with open(text_filepath, "w", encoding="utf-8") as text_file:
                text_file.write(extracted_text)
            
            print(f"Extracted text saved to {text_filepath}")

# Example usage
if __name__ == "__main__":
    folder_path = "images_folder"  # Change this to your folder path
    process_images_in_folder(folder_path)