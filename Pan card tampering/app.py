from flask import Flask, render_template, request
from model import calculate_ssim
import os 

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = 'static/uploads'

@app.route("/",methods=["GET","POST"])

def index():
    if request.method == "POST":
        file= request.files["image"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"],file.filename)
            file.save(filepath)
            score= calculate_ssim(filepath)
            return render_template("result.html", score = score, image_url = filepath)
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug = True)



