from Calculadora import Calculadora

# Criação de uma instância da classe Calculadora
calc = Calculadora(valorA=10, valorB=5, operacao='+')

# Chama o método para mostrar o resultado
calc.mostrarResultado()

# Teste com diferentes valores e operações
calc.valorA = 20
calc.valorB = 4
calc.operacao = '/'
calc.mostrarResultado()