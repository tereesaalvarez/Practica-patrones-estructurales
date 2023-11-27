class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

class UsuarioDatabase:
    def __init__(self):
        self.usuarios = []

    def añadir_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def encontrar_usuario(self, nombre_usuario, contraseña):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contraseña == contraseña:
                return True
        return False
    
