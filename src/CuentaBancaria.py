class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

    def consultar_saldo(self):
        return self.saldo


if __name__ == "__main__":
    cuenta = CuentaBancaria(100)
    cuenta.depositar(50)
    cuenta.retirar(30)
    print(f"Saldo final: {cuenta.consultar_saldo()}")
