from dotenv import load_dotenv
load_dotenv() #take environment variables from .env
import click
from flask import Flask, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
print("module:")
# print(redirect.__version__)
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/base/")
def base():
    return render_template("base.html")

@app.route("/read/")
def read():
    return render_template("read.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/conv/")
def conversation():
    return render_template("conv.html")

@app.route("/testimonials/")
def testimonials():
    return render_template("testimonials.html")

@app.route("/write/")
def write():
    return render_template("write.html")

@app.route("/about/")
def cred():
    return render_template("about.html")

@app.route("/toefl/")
def toefl():
    return render_template("toefl.html")

@app.route("/sci/")
def sci():
    return render_template("sci.html")

@app.route("/admin")
def admin():
    return redirect(url_for('user', name="Admin!"))


if __name__ == "__main__":
        app.run(debug=True)
