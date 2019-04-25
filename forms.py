from wtforms import Form, BooleanField, StringField, PasswordField, validators

class ContactForm(Form):
    name = StringField('Full Name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])