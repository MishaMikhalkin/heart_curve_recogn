import os
import process
from werkzeug.utils import secure_filename

from base64 import b64encode

from flask import Blueprint, flash, request, redirect, render_template, app
import configparser

app_routes = Blueprint('app_routes', __name__)

app_config = configparser.ConfigParser()
app_config.read('config.ini')


@app_routes.route('/show-heart-recognition', methods=['GET', 'POST'])
def detect_process():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)


        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            base_path = app_routes.root_path
            relative_path = app_config['heartscan'].get('upload_folder')
            # TODO: replace filename on UUID
            full_path = os.path.join(base_path, relative_path, filename)

            file.save(full_path)

            recognized_image, contour = process.process_image(full_path)
            b64img = b64encode(recognized_image).decode("utf-8")

            os.remove(full_path)
            return render_template("list.html", image=b64img)
    return render_template("upload.html")

def allowed_file(filename):
    extensions = app_config['heartscan'].get('allowed_extensions')
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extensions
