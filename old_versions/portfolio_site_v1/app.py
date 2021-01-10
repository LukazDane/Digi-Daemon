import secrets
from flask import Flask, g
from flask import render_template, flash, redirect, url_for, session, request, abort, send_file, make_response, current_app
import datetime
from datetime import date
from datetime import time
from datetime import datetime, timedelta
import os


DEBUG = True
PORT = int(os.environ.get('PORT', 9000))

app = Flask(__name__)


@app.route('/')
def index(name=None):

    return render_template('home.html')


@app.route('/Lukaz')
def about(name=None):
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
