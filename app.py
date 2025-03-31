import os
import random
from flask import Flask, render_template, jsonify, request, send_from_directory

# Create a Flask application
app = Flask(__name__)

# Directory for uploaded cat pictures
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Define a route for the root URL to render the HTML
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for Hello World API
@app.route('/getHelloWorld', methods=['GET'])
def hello_world():
    return jsonify(message='Hello, World!')

# Route to fetch a random cat picture
@app.route('/getCatPicture', methods=['GET'])
def get_cat_picture():
    files = os.listdir(UPLOAD_FOLDER)
    if not files:
        return jsonify(message='No cat pictures uploaded yet! 🐾')
    random_file = random.choice(files)
    return send_from_directory(UPLOAD_FOLDER, random_file)

# Route to upload a cat picture
@app.route('/uploadCatPicture', methods=['POST'])
def upload_cat_picture():
    if 'file' not in request.files:
        return jsonify(error='No file part in the request')
    
    file = request.files['file']
    if file.filename == '':
        return jsonify(error='No file selected')
    
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(message=f'Cat picture uploaded successfully: {filename}')
    else:
        return jsonify(error='Invalid file type. Only images are allowed.')

# Check allowed file types
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)