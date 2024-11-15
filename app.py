from flask import Flask, request, send_from_directory, render_template
import os
from flask import redirect

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def upload_form():
    return render_template('upload.html', files=os.listdir(UPLOAD_FOLDER))

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return 'File uploaded successfully!'

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/delete/<path:filename>')
def delete_file(filename):
    try:
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        return 'File deleted successfully!'
    except Exception as e:
        return str(e)
@app.route('/rename', methods=['GET', 'POST'])
def rename_file():
    if request.method == 'POST':
        old_filename = request.form.get('old_filename')
        new_filename = request.form.get('new_filename')

        try:
            if os.path.exists(os.path.join(UPLOAD_FOLDER, old_filename)):
                os.rename(os.path.join(UPLOAD_FOLDER, old_filename), os.path.join(UPLOAD_FOLDER, new_filename))
                return 'File renamed successfully!'
            else:
                return 'File does not exist.'
        except Exception as e:
            return str(e)

    return redirect('/')

if __name__ == '__main__':
    app.run(port=5012, debug=True)
