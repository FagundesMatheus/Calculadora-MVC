def defAB(expressao):
    a = None
    b = None
    IOperacao = None
    operacoes = ['+', '-', '×', '/', '^', '÷']
    for i in range(len(expressao)):
        if expressao[i] in operacoes and i != 0:
            a = expressao[:i]
            b = expressao[i+1:]
            IOperacao = i
            break
    return a, b, IOperacao

def resolver(expressao):
    print(expressao)
    print("bbbbbb")
    a = None
    b = None

    a, b, IOperacao = defAB(expressao)
    if 'sqrt' in expressao:
        print('tem sqrt')
        numero = expressao[expressao.index('(') + 1: expressao.index(')')]
        resposta = raiz(float(numero))
        expressao = expressao.replace(f"sqrt({numero})", str(resposta))




    if '%' in expressao:
        print('tem percento')
        print('a:' + a + ' b:' + b)
        if b is None:
            return 0
        else:
            print('else')
            print(porcentagem(float(b[:-1])))
            if expressao[IOperacao] == '/' or expressao[IOperacao] == '÷' or expressao[IOperacao] == '×':
                expressao = expressao.replace(b, str(porcentagem(float(b[:-1]))))
            else:
                expressao = expressao.replace(b, str(porcentagem(float(b[:-1])) * int(a)))
            print('expressão:' + expressao)
            a, b, IOperacao = defAB(expressao)
    elif b is None:
        return expressao
    print('expressão:' + expressao)
    print(a, b)
    a, b = float(a), float(b)

    if expressao[IOperacao] == '+':
        return soma(a, b)
    elif expressao[IOperacao] == '-':
        return subtracao(a, b)
    elif expressao[IOperacao] == '×':
        return multiplicacao(a, b)
    elif expressao[IOperacao] == '/' or expressao[IOperacao] == '÷':
        return divisao(a, b)
    elif expressao[IOperacao] == '^':
        return potencia(a, b)


    return expressao





def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b
def potencia(a, b):
    return a ** b
def raiz(a):
    return a ** (1 / 2)
def porcentagem(a):
    return a / 100
