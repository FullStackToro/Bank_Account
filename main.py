
if __name__ == '__main__':
    class bankAccount:
        def __init__(self, interes):
            self.interes = interes
            self.saldo=0

        def deposito(self, monto):
            self.saldo += monto
            return self

        def retiro(self, monto):
            if self.saldo >= monto:
                self.saldo -= monto
            elif monto>self.saldo:
                print('Fondos insuficientes: cobrar una tarifa de $5')
                self.saldo -= 5
            return self

        def accountInfo(self):
            print('*'*45, '\n Interés:', self.interes, '%' '\n Saldo: $', self.saldo, '\n', '*'*44,)
            return self

        def tasa_interes(self):
            self.saldo = self.saldo+self.saldo*self.interes/100
            return self

    c1=bankAccount(2)
    c2=bankAccount(1.5)

    c1.deposito(2000).deposito(4000).deposito(5000).retiro(1000).tasa_interes().accountInfo()
    c2.deposito(12000).deposito(34000).retiro(5000).retiro(1000).tasa_interes().accountInfo()