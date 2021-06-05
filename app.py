from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)


app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return 'Hello World!'


@app.route('/random')
def random():
    return 'Hello World!'


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print("klik")
        email = request.form["email"]
        message = request.form["message"]
        print(email)

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
