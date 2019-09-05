from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resume.html")
def resume():
    return render_template("resume.html")

@app.route("/blog.html")
def blog():
    return render_template("blog.html")

@app.route("/bucket.html")
def bucketlist():
    return render_template("bucket.html")

if __name__ == "__main__":
    app.run(debug=True)