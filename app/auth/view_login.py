from . import auth
from flask import render_template, redirect, url_for, session, flash, make_response
from app.forms import LoginForm
from flask_login import login_required
from app.firebase_service import get_user


@auth.route('/logeo', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usuario registrado con éxito!')
        return redirect(url_for('auth.session_page'))
    return render_template('login.html', **context)

@auth.route('/session')
@login_required
def session_page():
    return render_template('plataform.html')


