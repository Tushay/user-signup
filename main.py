from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route ("/")
def index():
    return render_template('homepage.html')


@app.route("/", methods=['POST'])
def user():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']







app.run()


