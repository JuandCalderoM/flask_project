from . import auth
from flask import render_template, redirect, url_for, session, flash
from app.forms import LoginForm,Signup,Publicacion,Delete
from app.firebase_service import  get_user_exit ,put_user,get_blog,put_blog,get_blog_reference,get_user_edit,get_commit,delete_commit,delete_blog
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date,datetime
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        # Obtener los datos del usuario (incluyendo la contraseña encriptada) desde la base de datos
        user = get_user_exit(username)
        
        if user:
            # Verificar la contraseña ingresada con la contraseña encriptada almacenada
            if check_password_hash(user['clave_usuario'], password):  # Aquí se asume que 'clave_usuario' es la contraseña encriptada
                session['username'] = username
                flash('Inicio de sesión exitoso!')
                return redirect(url_for('auth.session_page'))
            else:
                flash('Nombre de usuario o contraseña incorrectos')
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
    delete_form=Delete()
    commit=get_commit()
    context = {
        'username': username,
        'commit':commit,
        'delete_form':delete_form
    }
    if username:
        return render_template('view_comment.html', **context)
    else:
        flash("Necesitas iniciar sesión :)")
        return redirect(url_for('auth.login'))
    
@auth.route('/delete_commit/<string:id>', methods=['POST'])
def delete_commit(id):
    delete_commit(id)
    return redirect(url_for('auth.comentario'))

@auth.route('/usuarios')
def usuarios():
    username = session.get('username')
    user=get_user_edit(username)
    context={
        'username':username,
        'user':user
    }
    if username:
        return render_template('usuarios.html',**context)
    else:
        flash("necesistas de un inicio de sesion :)")
        return redirect(url_for('auth.login'))
@auth.route('/crear_user',methods=['GET', 'POST'])
def crear_user():
    username = session.get('username')
    signup=Signup()
    context={
        'username':username,
        'signup':signup
    }
    if username:
        if signup.validate_on_submit():
            usuario_data=signup.username.data
            password_data=signup.password.data
            rol_usuario="admnin"
            correo_usuario=signup.email.data
            uaerdoc=get_user_exit(usuario_data)
            if not uaerdoc:  # Verifica si la lista está vacía
                password_secury=generate_password_hash(password_data)
                put_user(password_secury,correo_usuario,usuario_data,rol_usuario)
                flash('Usuario registrado!')
                return redirect(url_for('auth.usuarios'))
            else:
                flash('este usuario ya esta registrado!')  
                return redirect(url_for('auth.crear_user'))
        return render_template('createuser.html',**context)
    else:
        flash("necesistas de un inicio de sesion :)")
        return redirect(url_for('auth.login'))

    
    
@auth.route('/crear_pub',methods=['GET', 'POST'])
def crear_pub():
    username = session.get('username')
    publication=Publicacion()
    context={
        'username':username,
        'publi':publication
    }
    if username:
        if publication.validate_on_submit():
            title=publication.title.data
            historia=publication.historia.data
            observacion=publication.observacion.data
            fecha=date.today()
            fecha_publicacion = datetime.combine(fecha, datetime.min.time())  # Convertir a datetime
            id=username+title
            publicdoc=get_blog(id)
            if not publicdoc:
                put_blog(id,title,username,observacion,historia,fecha_publicacion)
                flash('Publicacion registrada!')  
                return redirect(url_for('auth.ver_pub'))
            else:
                flash('Ya realizaste esta publicacion')  
                return redirect(url_for('auth.crear_pub'))
        return render_template('publicaciones.html',**context)
    else:
        flash("necesistas de un inicio de sesion :)")
        return redirect(url_for('auth.login'))
@auth.route('/ver_pub')
def ver_pub():
    username = session.get('username')
    blogs = get_blog_reference(username)
    delete_form=Delete()
    # Formatear fecha si es necesario
    for blog in blogs:
        if 'fecha_publicacion' in blog:
            # Verificar si 'fecha_publicacion' es del tipo DatetimeWithNanoseconds o similar
            if isinstance(blog['fecha_publicacion'], datetime):
                blog['fecha_publicacion'] = blog['fecha_publicacion'].strftime('%d/%m/%Y')
    
    context = {
        'username': username,
        'blogs': blogs,
        'delete_form':delete_form
    }
    
    if username:
        return render_template('ver_public.html', **context)
    else:
        flash("Necesitas un inicio de sesión :)")
        return redirect(url_for('auth.login'))
@auth.route('/delete_p/<string:id>', methods=['POST'])
def delete_pub(id):
    delete_blog(id)
    return redirect(url_for('auth.ver_pub'))

@auth.route('/volver')
def volver():
    return redirect(url_for('main.index'))