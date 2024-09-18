import os
import firebase_admin
from firebase_admin import credentials, firestore
from werkzeug.security import  check_password_hash
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
    
    query = users_ref.where('nombre_usuario', '==', usuario).where(check_password_hash(['clave_usario'],clave)).stream()

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
        return user_data # 
    return None  # Si no se encuentra el usuario  # Devuelve el rol del usuario
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

# Ejemplo de uso