from flask import Flask,request, make_response,redirect, render_template,session,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email
app=Flask(__name__)
app.config['SECRET_KEY']='SUPER SECRETO'
bootstrap = Bootstrap(app)
class ContactForm(FlaskForm):
    name=StringField('Nombre',validators=[DataRequired()])
    email=StringField('Correo Electronico',validators=[DataRequired(), Email()])
    subject=StringField('Tema',validators=[DataRequired()])
    comments=TextAreaField('commentario',validators=[DataRequired()])
    enviar=SubmitField('Enviar')

@app.route('/')
def index():
    return render_template('inicio.html')


@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/anuncios')
def anuncios():
    return render_template('anuncios.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route("/verficarComentPost")
def post_aprob_coment():
    response = make_response(redirect('/contactanos'))
    return response
@app.route("/contactanos", methods=['GET','POST'])

def contactanos_view():
    form = ContactForm()
    context={
        'form':form
    }
    if form.validate_on_submit():
        name = form.name.data
        session['name'] = name
        flash('Muchas gracias por la sugerencia!')
        return redirect(url_for('contactanos_view'))  
    return render_template('comentario.html', **context)
@app.errorhandler(404)
def not_found(error):
    context = {
        'code': 404,
        'message_for_error' : 'Not Found',
        'error' : error
    }
    return render_template('error.html', **context)

@app.errorhandler(500)
def internal_server_error(error):
    context = {
        'code': 500,
        'message_for_error' : 'Internal Server Error',
        'error' : error
    }
    return render_template('error.html', **context)

if __name__ == '__main__':
    app.run()



