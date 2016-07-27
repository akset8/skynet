

import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

import cnn_fast
import cnn


app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'uploads/'

app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/upload', methods=['POST'])
def upload():
    
    uploaded_files = request.files.getlist("file[]")
    filenames = []
    for file in uploaded_files:
        
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename)
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           
            filenames.append(filename)
            print (len(filenames))

    if(len(filenames)==2):
        
        res =  (cnn_fast.eval1("uploads/"+filenames[0],"uploads/"+filenames[1]))
         
    return render_template('upload.html', filename1="uploads/"+filenames[0] , filename2 ="uploads/"+filenames[1], result=res)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    )


