from flask_login import UserMixin
from .firebase_service import get_user_by_key_and_password

class UserData:
    def __init__(self, username, password, email, role):
        self.username = username
        self.password = password
        self.email = email
        self.role = role

class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password
        self.email = user_data.email
        self.role = user_data.role

    @staticmethod
    def query(username, password):
        # Utiliza el método para obtener el usuario desde Firestore
        user_data = get_user_by_key_and_password(username, password)
        if user_data:
            return UserModel(UserData(
                username=user_data['nombre_usuario'],
                password=user_data['clave_usario'],
                email=user_data['correo_usuario'],
                role=user_data['rol_usario']
            ))
        return None  # Si no se encuentra el usuario
  