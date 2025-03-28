import pytest
from src.cuenta_bancaria import CuentaBancaria

def test_depositar():
    cuenta = CuentaBancaria(100)
    assert cuenta.depositar(50) == True
    assert cuenta.consultar_saldo() == 150

def test_retirar():
    cuenta = CuentaBancaria(100)
    assert cuenta.retirar(50) == True
    assert cuenta.consultar_saldo() == 50

def test_retirar_sin_fondos():
    cuenta = CuentaBancaria(30)
    assert cuenta.retirar(50) == False
    assert cuenta.consultar_saldo() == 30

