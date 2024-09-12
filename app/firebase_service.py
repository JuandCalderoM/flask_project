import os
import firebase_admin
from firebase_admin import credentials, firestore

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(BASE_DIR, 'config', 'firebase_key.json')

# Inicializa la aplicación Firebase
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Configura Firestore
db = firestore.client()

def get_user():
    db.collection('usuario').get()
def get_user_by_key_and_password(usuario, clave):
    # Realizar una consulta en Firestore donde 'clave_usuario' y 'password' coincidan
    users_ref = db.collection('usuario')  # El nombre de tu colección en Firebase
    query = users_ref.where('nombre_usuario', '==', usuario).where('clave_usario', '==', clave).stream()

    # Iterar sobre los resultados (debería haber solo uno si las claves son únicas)
    for user in query:
        user_data = user.to_dict()
        return user_data  # Devuelve los datos del usuario encontrado
    return None  # Si no se encuentra el usuario
def get_user_rol(usuario):
    users_ref = db.collection('usuario')
    query = users_ref.where('nombre_usuario', '==', usuario)
    for user in query:
        user_data = user.to_dict()
        return user_data.get('rol')  # Devuelve solo el rol del usuario
    return None  # Si no se encuentra el usuario  # Devuelve el rol del usuario

    
    