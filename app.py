# from flask import Flask, render_template, request, jsonify, send_from_directory
# from werkzeug.utils import secure_filename
# import os

# from predict import predict_emotion

# from flask import jsonify
# import numpy as np

# UPLOAD_FOLDER = 'D:\Workspace\ED\Emotion_Detection_ML\Local Data'  # Specify the path to the folder where uploaded files will be stored
# ALLOWED_EXTENSIONS = {'wav'}  # Specify the allowed file extensions

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




# # Route to serve the accuracy.json file from the static directory
# @app.route('/accuracy.json')
# def serve_accuracy_json():
#     return send_from_directory(app.static_folder, 'accuracy.json')

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})
#     if file and allowed_file(file.filename):
#         # Securely save the uploaded file to a temporary location
#         uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
#         file.save(uploaded_file_path)

#         # Call emotion detection function with the uploaded file path
#         detected_emotion = predict_emotion(uploaded_file_path)

#         # Remove the uploaded file from the temporary location
#         os.remove(uploaded_file_path)

#         # Convert the NumPy array to a Python list before serializing it
#         detected_emotion_list = detected_emotion.tolist()

#         return jsonify({'emotion': detected_emotion_list})
#     else:
#         return jsonify({'error': 'Invalid file type'})

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os

from predict import predict_emotion

UPLOAD_FOLDER = 'D:/Workspace/ED/Emotion_Detection_ML/Local Data'  # Specify the path to the folder where uploaded files will be stored
ALLOWED_EXTENSIONS = {'wav'}  # Specify the allowed file extensions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Route for serving accuracy.html
@app.route('/accuracy')
def accuracy():
    return render_template('accuracy.html')


# Route for serving accuracy.json
@app.route('/accuracy.json')
def serve_accuracy_json():
    accuracy_data = {
        "random_forest": 99.643,
        "decision_tree": 91.071,
        "naive_bayes": 80.0,
        "mlp": 99.286
    }
    return jsonify(accuracy_data)


# Route for serving upload.html
@app.route('/upload_page')
def upload_page():
    return render_template('upload.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and allowed_file(file.filename):
        # Securely save the uploaded file to a temporary location
        uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(uploaded_file_path)

        # Call emotion detection function with the uploaded file path
        detected_emotion = predict_emotion(uploaded_file_path)

        # Remove the uploaded file from the temporary location
        os.remove(uploaded_file_path)

        # Convert the NumPy array to a Python list before serializing it
        detected_emotion_list = detected_emotion.tolist()

        return jsonify({'emotion': detected_emotion_list})
    else:
        return jsonify({'error': 'Invalid file type'})



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




if __name__ == '__main__':
    app.run(debug=True)
