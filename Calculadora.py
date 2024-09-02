class Calculadora:
    def __init__(self, valorA=0, valorB=0, operacao=''):
        self._valorA = valorA
        self._valorB = valorB
        self._operacao = operacao

    @property
    def valorA(self):
        return self._valorA

    @valorA.setter
    def valorA(self, valor):
        self._valorA = valor

    @property
    def valorB(self):
        return self._valorB

    @valorB.setter
    def valorB(self, valor):
        self._valorB = valor

    @property
    def operacao(self):
        return self._operacao

    @operacao.setter
    def operacao(self, operacao):
        self._operacao = operacao

    def validarOperacao(self, operacao):
        if operacao in ['+', '-', '*', '/']:
            return True
        else:
            return False

    def calcular(self):
        if not self.validarOperacao(self.operacao):
            print("Operação inválida!")
            exit(1)
        
        if self.operacao == '+':
            return self.valorA + self.valorB
        elif self.operacao == '-':
            return self.valorA - self.valorB
        elif self.operacao == '*':
            return self.valorA * self.valorB
        elif self.operacao == '/':
            if self.valorB == 0:
                print("Divisão por zero não é permitida!")
                exit(1)
            return self.valorA / self.valorB

    def mostrarResultado(self):
        print(f"{self.valorA} {self.operacao} {self.valorB} = {self.calcular()}")

