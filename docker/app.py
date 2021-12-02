# flask_web/app.py
from flask import Flask
from flask import render_template
from flask.globals import request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        my_file = open("/storage/test.txt", "w+")
        my_file.write("Test text written to the file")
        my_file.close()
        return render_template("index.html")
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
