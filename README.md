```markdown
# Python QRCode Generator

## Overview
The Python QRCode Generator is a simple tool designed to generate QR codes from user-provided sentences. The project includes functionalities for inserting sentences into a database, removing them, and generating QR codes from the stored sentences. The QR codes can be used for various purposes such as embedding URLs, text, or any other information that can be encoded.

## Features
- Insert sentences into a database.
- Remove sentences from the database.
- Generate QR codes from stored sentences.
- Display generated QR codes.

## Installation Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/jonathas/pyqrcodegenerator.git
   cd pyqrcodegenerator
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python pyqrcodegenerator.py
   ```

## Usage Examples
Once you run the application, use the menu to interact with the tool.

**Example Menu:**
```
QRCode Generator

1) Generate QRCode from sentence
2) Insert a sentence
3) Remove a sentence
4) Exit

Type your option: 
```

**Generating a QR Code:**
1. Choose option `1` and follow the prompts to select and generate a QR code from an existing sentence.
   
**Inserting a Sentence:**
1. Choose option `2` and follow the prompts to insert a new sentence into the database.

**Removing a Sentence:**
1. Choose option `3` and follow the prompts to remove an existing sentence from the database.

**Viewing a Generated QR Code in Code:**
```python
import pyqrcode

URL = "http://www.example.com/"
qr_image = pyqrcode.MakeQRImage(URL, rounding=5, fg="black", bg="burlywood", br=False)
qr_image.show()
```

## Code Summary
- **`controller.py`**:
  - Contains the `Menu` class which handles user interaction and commands.
  
- **`model.py`**:
  - Contains the `Sentences` class which handles the database interactions for storing, retrieving, and deleting sentences.
  
- **`pyqrcodegenerator.py`**:
  - Entry point of the application, creates an instance of the `Menu` class and displays the menu for user interaction.
  
- **`pyqrcode/__init__.py`**:
  - Initialization file for the `pyqrcode` module.
  
- **`pyqrcode/pyqrcode.py`**:
  - Contains the QR code generation logic, adapted from a JavaScript library.

- **`pyqrcode/setup.py`**:
  - Package setup script for the `pyqrcode` library.

- **`pyqrcode/test.py`**:
  - Test script for generating and displaying QR codes.

## Contributing Guidelines
1. **Fork the Repository**
   - Create your own fork of the project on GitHub.

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/jonathas/pyqrcodegenerator.git
   cd pyqrcodegenerator
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature-branch
   ```

4. **Make Your Changes**
   - Implement your feature or fix the bug.

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

6. **Push Your Changes**
   ```bash
   git push origin feature-branch
   ```

7. **Create a Pull Request**
   - Submit a pull request against the main repository.

## License
This project is licensed under the MIT License. For more details, refer to the `LICENSE` file in the repository.
```