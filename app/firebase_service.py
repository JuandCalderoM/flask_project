import os
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(BASE_DIR, 'config', 'firebase_key.json')

# Inicializa la aplicación Firebase
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Configura Firestore
db = firestore.client()

def get_user():
    # Obtener referencia a la colección
    usuarios_ref = db.collection('usuario')

    # Traer todos los documentos de la colección
    docs = usuarios_ref.stream()
    return docs
def get_user_by_key_and_password(usuario, clave):
    # Realizar una consulta en Firestore donde 'clave_usuario' y 'password' coincidan
    users_ref = db.collection('usuario')  # El nombre de tu colección en Firebase
    query = users_ref.where('nombre_usuario', '==', usuario).where('clave_usario', '==', clave).stream()

    # Iterar sobre los resultados (debería haber solo uno si las claves son únicas)
    for user in query:
        user_data = user.to_dict()
        return user_data  # Devuelve los datos del usuario encontrado
    return None  # Si no se encuentra el usuario
def get_user_exit(usuario):
    users_ref = db.collection('usuario')
    query = users_ref.where('nombre_usuario', '==', usuario).get()
    for user in query:
        user_data = user.to_dict()
        user_data['id'] = user.id
        return user_data # 
    return None  # Si no se encuentra el usuario  # Devuelve el rol del usuario
def get_user_edit(usuario):
    users_ref = db.collection('usuario')
    query = users_ref.where('nombre_usuario', '!=', usuario).get()
    users=[]
    for user in query:
        user_data = user.to_dict() 
        users.append(user_data)
    return users
def put_user(user_clav, correo_usuario, nombre_usuario, rol_usuario):
    # Referencia al documento del usuario
    user_doc_ref = db.collection('usuario').document(nombre_usuario)#no se como crear u id aleaotrorio
    
    # Datos a actualizar o insertar en el documento
    user_data = {
        'clave_usuario': user_clav,
        'correo_usuario': correo_usuario,
        'nombre_usuario': nombre_usuario,
        'rol_usuario': rol_usuario
    }
    # Usa el método 'set' para actualizar o crear el documento
    user_doc_ref.set(user_data, merge=True)  # merge=True permite combinar los datos con los existentes
    

##Sector de los comentarios
def get_comment(user_id):
    comment_ref = db.collection('comentario').document(user_id).get()
    # Verifica si el documento existe
    if comment_ref.exists:
        com_data = comment_ref.to_dict()  # Convierte los datos a un diccionario
        return com_data  # Retorna los datos del comentario
    else:
        return None

# generar un comentario
def put_commit(id,comments,subject,email,name):
    commit_doc_ref = db.collection('comentario').document(id)
    user_data = {
        'comments': comments,
        'email': email,
        'name': name,
        'subject': subject
    }
    # Usa el método 'set' para actualizar o crear el documento
    commit_doc_ref.set(user_data, merge=True) 
#muestro todos los comentarios
def get_commit():
    commit_ref = db.collection('comentario')
    query = commit_ref.get()
    
    commits = []
    for commit in query:
        commit_data = commit.to_dict()
        commit_data['id'] = commit.id  # Añadir el ID del documento
        commits.append(commit_data)

    return commits

#  función de eliminación
def delete_commit_from_firestore(id):
    if not id:
        return "ID no válido"

    try:
        commit_doc_ref = db.collection('comentario').document(id)
        commit_doc_ref.delete()
        return "Comentario eliminado exitosamente"
    except Exception as e:
        return f"Ocurrió un error al eliminar el comentario: {str(e)}"
#Seccion para el blogñ
def get_blog(id):
    blog_ref = db.collection('blog').document(id).get()
    # Verifica si el documento existe
    if blog_ref.exists:
        blog_data = blog_ref.to_dict()  # Convierte los datos a un diccionario
        return blog_data  # Retorna los datos del comentario
    else:
        return None
def get_blog_reference(user):
    blog_ref = db.collection('blog')
    query = blog_ref.where('publicador', '==', user).get()
    
    blogs = []
    for blog in query:
        user_data = blog.to_dict()
        user_data['id'] = blog.id
        # Si 'fecha_publicacion' es del tipo DatetimeWithNanoseconds, no se necesita convertirla
        blogs.append(user_data)

    return blogs

def get_all_blogs():
    # Obtén la referencia a la colección 'blog'
    blog_ref = db.collection('blog')
    
    # Realiza la consulta para obtener todos los documentos
    query = blog_ref.get()
    
    blogs = []
    for blog in query:
        # Convierte el documento a un diccionario
        blog_data = blog.to_dict()
        # Añade el diccionario a la lista de blogs
        blogs.append(blog_data)
    
    # Ordena la lista de blogs por 'fecha_publicacion' en orden descendente
    blogs_sorted = sorted(blogs, key=lambda x: x['fecha_publicacion'], reverse=True)
    
    return blogs_sorted
##generar un blog
def put_blog(id,title,username,observacion,historia,fecha_publicacion):
    commit_doc_ref = db.collection('blog').document(id)
    user_data = {
        'titulo_blog': title,
        'publicador': username,
        'observacion': observacion,
        'historia': historia,
        'fecha_publicacion':fecha_publicacion
    }
    # Usa el método 'set' para actualizar o crear el documento
    commit_doc_ref.set(user_data, merge=True) 
#borrar el blog
def delete_blog(id):
    blog_doc_ref = db.collection('blog').document(id)
    blog_doc_ref.delete()
#actualizar perfil
def updte_user_perfil(username, correo_usuario_actualizado, nueva_clave_hash):
    doc_user = get_user_exit(username)
    
    if doc_user:
        # Preparamos el diccionario para la actualización
        update_data = {
            'correo_usuario': correo_usuario_actualizado,
            'clave_usuario':nueva_clave_hash
        }
        db.collection('usuario').document(doc_user['id']).update(update_data)
        print(update_data)
    else:
        print("Usuario no encontrado")

#actualizar publicacion
def update_blog_base(user, titulo, nueva_observacion, nueva_historia, nueva_fecha_publicacion):
    # Obtén la referencia del blog a través del usuario
    blogs = get_blog_reference(user)
    
    if blogs:
        for blog in blogs:  # Itera sobre cada blog
                blog_doc_ref = db.collection('blog').document(blog['id'])

                # Datos que se van a actualizar
                update_data = {
                    'titulo_blog': titulo,
                    'observacion': nueva_observacion,
                    'historia': nueva_historia,
                    'fecha_publicacion': nueva_fecha_publicacion,
                }

                # Usa el método 'update' para actualizar el documento
                blog_doc_ref.update(update_data)
                return True  # Devuelve True si la actualización fue exitosa
    return False  # Devuelve False si no se encontró el blog
