from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<usr>')
def user(usr):
    return f"<h1> Welcome {usr} 👍</h1>"
    flash("Hi man", "info")

@app.route('/signin', methods= ["POST", "GET"])
def signin():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("signin.html")



if __name__ == "__main__":
    app.run(debug=True)









