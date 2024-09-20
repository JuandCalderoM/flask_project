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
class Signup(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    email=StringField('Correo del usuario', validators=[DataRequired(),Email()])
    submit = SubmitField('Crear Usuario')
class Publicacion(FlaskForm):
    title= StringField('Titulo de la publicacion', validators=[DataRequired()])
    historia=TextAreaField('Historia', validators=[DataRequired()])
    observacion=TextAreaField('Observacion', validators=[DataRequired()])
    submit = SubmitField('Crear Publicacion')
class Delete(FlaskForm):
    submit=SubmitField('Eliminar')