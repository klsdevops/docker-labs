import os
from flask import Flask, request, jsonify, render_template
import pytesseract
from PIL import Image
from werkzeug.utils import secure_filename
import tempfile

# Initialize the Flask application
app = Flask(__name__)

# Since Tesseract is installed directly in the container's environment (via Dockerfile), 
# it should be in the PATH, so we set the command explicitly here for clarity/robustness.
pytesseract.pytesseract.tesseract_cmd = 'tesseract'

@app.route('/')
def serve_index():
    """Serves the static HTML frontend."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handles image upload, performs OCR, and returns the text."""
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        # Create a secure filename and temporary path to save the file
        filename = secure_filename(file.filename)
        
        # Use tempfile to ensure cleanup, even though we manually delete later
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_path = os.path.join(tmpdir, filename)
            file.save(temp_path)
            
            extracted_text = ""
            
            try:
                # Open the image and perform OCR
                img = Image.open(temp_path)
                extracted_text = pytesseract.image_to_string(img)
                
                # Clean up the file (optional, as we are in a temporary directory)
                # os.remove(temp_path)
                
                return jsonify({'success': True, 'text': extracted_text})

            except pytesseract.TesseractNotFoundError:
                # This should not happen if the Dockerfile is correct, but good for robust error handling
                return jsonify({'error': 'Tesseract OCR engine not found in container.'}), 500
            except Exception as e:
                # Catch general image/OCR processing errors
                return jsonify({'error': f'OCR processing failed: {str(e)}'}), 500

    return jsonify({'error': 'Unknown error during file processing'}), 500

if __name__ == '__main__':
    # When running outside of the 'flask run' command (like in development)
    app.run(host='0.0.0.0', port=5000)
