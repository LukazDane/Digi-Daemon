import secrets
from flask import Flask, g
from flask import render_template, flash, redirect, url_for, session, request, abort, send_file, make_response, current_app
from wtforms import TextField, TextAreaField, SubmitField, StringField, PasswordField, IntegerField, FileField
from flask import make_response as response
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_bcrypt import check_password_hash
import datetime
from datetime import date
from datetime import time
from datetime import datetime, timedelta
from peewee import fn
from io import BytesIO
from PIL import Image
import urllib
from markupsafe import Markup
import os
import forms 
import models

DEBUG = True
PORT = int(os.environ.get('PORT', 9000))

app = Flask(__name__)
app.secret_key = 'elsdhfsdlfdsjfkljdslfhjlds'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/lukazphelps/Desktop/Grapplr/grapplr.db'
db = SQLAlchemy(app)

@app.route('/')
def index(name=None):
        return render_template('home.html')

@app.route('/Lukaz')
def about(name=None):
        return render_template('about.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=DEBUG, port=PORT)
