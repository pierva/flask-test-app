#!/usr/bin/env python3

import os
from flask import Flask, url_for, render_template


app = Flask(__name__)

@app.route('/home')
def showHome():
    return render_template('home.html')


@app.route('/about')
def showAbout():
    return render_template('about.html')


@app.route('/login')
def showLogin():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
