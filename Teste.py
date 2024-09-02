class Calculadora:
    def __init__(self, valorA=0, valorB=0, operacao=''):
        self._valorA = valorA
        self._valorB = valorB
        self._operacao = operacao

    # (outros métodos permanecem os mesmos...)

    def entradaDados(self):
        self.valorA = float(input("Digite o valor A: "))
        self.valorB = float(input("Digite o valor B: "))
        self.operacao = input("Digite a operação (+, -, *, /): ")

# No script `main_calculadora.py`:

from Calculadora import Calculadora

calc = Calculadora()

# Solicita ao usuário para inserir os dados
calc.entradaDados()

# Chama o método para mostrar o resultado
calc.mostrarResultado()