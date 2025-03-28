class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar(self, usuario, contrasena):
        if usuario in self.usuarios:
            return False
        self.usuarios[usuario] = contrasena
        return True

    def autenticar(self, usuario, contrasena):
        return self.usuarios.get(usuario) == contrasena


if __name__ == "__main__":
    sistema = SistemaUsuarios()
    sistema.registrar("usuario1", "clave123")
    print(f"Autenticación correcta: {sistema.autenticar('usuario1', 'clave123')}")
