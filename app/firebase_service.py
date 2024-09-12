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
