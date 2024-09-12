# app/routes.py
from . import main
from flask import render_template, redirect, url_for, session, flash
from app.forms import ContactForm


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



@main.route("/contactanos", methods=['GET', 'POST'])
def contactanos_view():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        session['name'] = name
        flash('Muchas gracias por la sugerencia!')
        return redirect(url_for('main.contactanos_view'))
    return render_template('comentario.html', form=form)
@main.route('/go-to-login')
def go_to_login():
    # Aquí rediriges al blueprint `auth`, a la ruta `login`
    return redirect(url_for('auth.login'))

