from . import auth
from flask import render_template, redirect, url_for, session, flash
from app.forms import LoginForm
from app.models import UserModel
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        
        user = UserModel.query(username, password)
        if user:
            session['username'] = username
            flash('Inicio de sesión exitoso!')
           
            return redirect(url_for('auth.session_page'))
        else:
            flash('Nombre de usuario o contraseña incorrectos')

    return render_template('login.html', **context)
@auth.route('/session')
def session_page():
    username = session.get('username')
    context={
        'username':username
    }
    if username:
        return render_template('perfil.html', **context)
    else:
        flash("necesistas de un inicio de sesion :)")
        return redirect(url_for('auth.login'))
@auth.route('/logout')
def logout():
    session.clear()  # Elimina todas las variables de sesión
    flash("Sesion finalizada")
    return redirect(url_for('main.index'))
@auth.route('/perfil')
def perfil():
    username = session.get('username')
    context={
        'username':username
    }
    if username:
        return render_template('perfil.html', **context)
    else:
        flash("necesistas de un inicio de sesion :)")
        return redirect(url_for('auth.login'))


@auth.route('/comentario')
def comentario():
    username = session.get('username')
    context={
        'username':username
    }
    if username:
        return render_template('view_comment.html')
    else:
        flash("necesistas de un inicio de sesion :)")
        return redirect(url_for('auth.login'))

@auth.route('/usuarios')
def usuarios():
    username = session.get('username')
    context={
        'username':username
    }
    if username:
        return render_template('usuarios.html')
    else:
        flash("necesistas de un inicio de sesion :)")
        return redirect(url_for('auth.login'))
@auth.route('/crear_user')
def crear_user():
    username = session.get('username')
    context={
        'username':username
    }
    if username:
        return render_template('createuser.html')
    else:
        flash("necesistas de un inicio de sesion :)")
        return redirect(url_for('auth.login'))
@auth.route('/crear_pub')
def crear_pub():
    username = session.get('username')
    context={
        'username':username
    }
    if username:
        return render_template('publicaciones.html')
    else:
        flash("necesistas de un inicio de sesion :)")
        return redirect(url_for('auth.login'))
@auth.route('/volver')
def volver():
    return redirect(url_for('main.index'))