# app/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, make_response
from .forms import ContactForm
from app.firebase_service import put_commit,get_comment,get_all_blogs
from datetime import date,datetime
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
    blogs = get_all_blogs()
    # Formatear fecha si es necesario
    for blog in blogs:
        if 'fecha_publicacion' in blog:
            # Verificar si 'fecha_publicacion' es del tipo DatetimeWithNanoseconds o similar
            if isinstance(blog['fecha_publicacion'], datetime):
                blog['fecha_publicacion'] = blog['fecha_publicacion'].strftime('%d/%m/%Y')
    context = {
        'blogs': blogs,
    }
    return render_template('blog.html', **context)

@main.route("/verficarComentPost")
def post_aprob_coment():
    response = make_response(redirect('/contactanos'))
    return response

@main.route("/contactanos", methods=['GET', 'POST'])
def contactanos_view():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email= form.email.data
        subject=form.subject.data
        comments=form.comments.data
        id=email+subject
        contacto=get_comment(id)
        if not contacto:
            put_commit(id,comments,subject,email,name)
            flash('Muchas gracias por la sugerencia!')
            return redirect(url_for('main.contactanos_view'))
        else:
            flash('Ya nos registraste este comentario, espera a que lo resolvamos')
            return redirect(url_for('main.contactanos_view'))

    return render_template('comentario.html', form=form)

@main.route('/go-to-login')
def go_to_login():
    return redirect(url_for('auth.login'))