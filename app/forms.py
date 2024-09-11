from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    subject = StringField('Tema', validators=[DataRequired()])
    comments = TextAreaField('Comentario', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')