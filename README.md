### PDF to Image Converter

A Python script that **converts PDF pages into images** using **pdf2image**.  
The script processes PDFs and **saves each page as a JPEG image**, returning a structured **JSON output**.

---

## 🚀 Features
- Converts **each page** of a PDF into an image.
- Uses a **temporary directory** to avoid cluttering the file system.
- Handles **errors gracefully**, ensuring robust performance.
- Returns **structured JSON output** for easy integration.

---

## 🔧 **Installation**

### **1. Install Python and Required Libraries**
Ensure Python is installed. If not, download it from [Python.org](https://www.python.org/downloads/).

Then, install the required dependencies:

```sh
pip3 install pdf2image pillow
```

Additionally, install **Poppler** for PDF-to-image conversion:

#### **Windows**
1. Download **Poppler for Windows**: [Download Here](https://github.com/oschwartz10612/poppler-windows/releases/)
2. Extract it and **add the `bin` folder to system PATH**.
3. Verify installation:
   ```sh
   where poppler
   ```

#### **Linux (Ubuntu)**
```sh
sudo apt update
sudo apt install poppler-utils
```

#### **Mac (Homebrew)**
```sh
brew install poppler
```

---

## 🎯 **Running the Script**
### **Step 1: Clone the Repository**
```sh
git clone https://github.com/bharatcj/pdf-to-image-converter.git
cd pdf-to-image-converter
```

### **Step 2: Run the Script**
```sh
python3 pdf_to_image.py <pdf_file_path>
```
Replace `<pdf_file_path>` with the path to your PDF file.

**Example:**
```sh
python3 pdf_to_image.py sample.pdf
```

---

## 📜 **Example Output**
### **For a PDF with 3 Pages**
```json
{
    "status": "success",
    "converted_images": [
        "/tmp/page_1.jpg",
        "/tmp/page_2.jpg",
        "/tmp/page_3.jpg"
    ]
}
```

---

## ⚠️ **Error Handling**
If an error occurs:
- The script prints a **detailed error message**.
- It verifies **file existence** before processing.
- Returns **formatted JSON responses** for easy debugging.

---

## 🔄 **Customization**
- Modify `pdf_to_image.py` to change the **image format** (default: JPEG).
- Adjust **temporary directory settings** if needed.

---

## 🛡️ **License**
This project is licensed under the **MIT License**.

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to **fork this repository** and submit pull requests.

---

### **Author**
Developed by **Bharat CJ**  
GitHub: https://github.com/bharatcj

---

💡 **Did you know?** This script can be used for **OCR preprocessing**, making it easier to extract text from PDFs using tools like **Tesseract** or **EasyOCR**! 🚀📄