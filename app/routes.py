# app/routes.py
from flask import Blueprint, render_template, redirect, url_for, session, flash, make_response
from .forms import ContactForm,LoginForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('inicio.html')

@main.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@main.route('/anuncios')
def anuncios():
    return render_template('anuncios.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')

@main.route("/verficarComentPost")
def post_aprob_coment():
    response = make_response(redirect('/contactanos'))
    return response

@main.route("/contactanos", methods=['GET', 'POST'])
def contactanos_view():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        session['name'] = name
        flash('Muchas gracias por la sugerencia!')
        return redirect(url_for('main.contactanos_view'))

    return render_template('comentario.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usario registrado con éxito!')
        return redirect(url_for('main.login'))
    return render_template('login.html', **context)
@main.errorhandler(404)
def not_found(error):
    return render_template('error.html', code=404, message_for_error='Not Found', error=error)

@main.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', code=500, message_for_error='Internal Server Error', error=error)
