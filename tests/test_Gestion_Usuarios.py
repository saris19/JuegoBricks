import pytest
from main import SistemaUsuarios

def test_registro_usuario():
    sistema = SistemaUsuarios()
    assert sistema.registrar("usuario1", "clave123") == True
    assert sistema.registrar("usuario1", "otraClave") == False

def test_autenticacion_exitosa():
    sistema = SistemaUsuarios()
    sistema.registrar("usuario1", "clave123")
    assert sistema.autenticar("usuario1", "clave123") == True

def test_autenticacion_fallida():
    sistema = SistemaUsuarios()
    sistema.registrar("usuario1", "clave123")
    assert sistema.autenticar("usuario1", "claveIncorrecta") == False
