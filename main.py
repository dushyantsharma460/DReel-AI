# This file takes care of creating unique folder for the user upload file  

from flask import Flask, render_template , request
import uuid   # It is used to generate unique id | With the help of uuid we will upload the files to folder
import os

# Use werkzeug module to import secure file 
# Take this code from werkzeug
# Use docs -> https://flask.palletsprojects.com/en/stable/patterns/fileuploads/
            
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_upload'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Using eleven labs for sound creations  (text  ->  Sound)
# Link - https://elevenlabs.io/


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create" , methods=['GET','POST']) # Hanling post request
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        # print(request.files)
        # print(request.files.keys())

        # Get the uuid in the main file to use them             
        # print(request.form.get("uuid"))   
        req_id = request.form.get("uuid")

        # Get the text to the main file 
        # print(request.form.get("text"))
        desc = request.form.get("text")

        input_files = []
    
        # Now the next step is to upload these images to the appropreate files
        for key, value in request.files.items():  # We are taking the files and upload to a folder with the help of uuid
            print(key, value)
            # Upload the file to my folder one by one 
            # To upload the file use flask docs
            # Use docs -> https://flask.palletsprojects.com/en/stable/patterns/fileuploads/
            # Here the logic of upload folder via flask 

            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], req_id)))):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], req_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], req_id, filename))
                input_files.append(file.filename)

                # We will successfully created a folder uuid and in this folder all file that i upload from ui it will show 

            # Now the step is to capture the description and save it to the file
            with open(os.path.join(app.config['UPLOAD_FOLDER'], req_id, "desc.txt"), "w") as f:
                f.write(desc)
        for fl in input_files:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], req_id, "input.txt"), "a") as f:
                f.write(f"file '{fl}'\nduration 1\n")


    return render_template("create.html", myid = myid)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)