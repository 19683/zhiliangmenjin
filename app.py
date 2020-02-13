# coding: utf-8

from flask import Flask
from flask import render_template, url_for, redirect
from flask import request, session


app = Flask(__name__)  # type: Flask


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/test/', methods=['POST', 'GET'])
def test():
    return render_template('test.html')


app.secret_key = 'zxcvbnm,./'

if __name__ == '__main__':
    app.debug = True
    app.run()
