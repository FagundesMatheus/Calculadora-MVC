class Calculadora:
    def __init__(self):
        self.inputAtual = 0
        self.inputPassado = None


    def limparAtual(self):
        self.inputAtual = 0

    def limparTotal(self):
        self.inputAtual = 0
        self.inputPassado = None

    def soma(self, a, b):
        return a + b
    def subtracao(self, a, b):
        return a - b
    def multiplicacao(self, a, b):
        return a * b
    def divisao(self, a, b):
        return a / b
    def potencia(self, a):
        return a ** 2
    def raiz(self, a):
        return a ** (1 / 2)
    def dividirPraUm(self, a):
        return 1 / a
    def porcentagem(self, a):
        return a / 100
