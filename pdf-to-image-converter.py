import sys
import json
import os
from pdf2image import convert_from_path
from tempfile import TemporaryDirectory

def convert_pdf_to_images(pdf_file):
    """
    Converts a PDF into images, saving each page as a separate JPEG file.

    Args:
        pdf_file (str): Path to the PDF file.

    Returns:
        dict: JSON response with converted image filenames or an error message.
    """
    try:
        # Check if the file exists before processing
        if not os.path.exists(pdf_file):
            return json.dumps({"status": "error", "message": f"File not found: {pdf_file}"})

        converted_images = []

        # Use a temporary directory for storing images
        with TemporaryDirectory() as temp_dir:
            images = convert_from_path(pdf_file, output_folder=temp_dir)

            for i, image in enumerate(images):
                image_file = os.path.join(temp_dir, f"page_{i + 1}.jpg")
                image.save(image_file, 'JPEG')
                converted_images.append(image_file)

        return json.dumps({"status": "success", "converted_images": converted_images})

    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})

if __name__ == "__main__":
    """
    Command-line execution of the script.
    Usage:
        python3 pdf_to_image.py <pdf_file_path>
    """
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "No PDF file path provided"}))
        sys.exit(1)

    pdf_file_path = sys.argv[1]
    print(convert_pdf_to_images(pdf_file_path))