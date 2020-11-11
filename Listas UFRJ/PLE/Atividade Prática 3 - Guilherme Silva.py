#Questão 1
def absoluto(arg):
    """Função que retorna o valor absoluto de um número sem a utilização de da função abs. Entrada int,float ou str -> float"""
    arg = str(arg)
    arg = float(arg.replace('-',''))
    return arg
#Questão 2
def quantidade_raizes(a,b,c):
    """Função que retorna a quantidade de raízes de uma função do 2ª grau. int,float -> int"""
    delta = b**2-4*a*c
    if delta < 0:
        return 0
    elif delta == 0:
        return 1
    else:
        return 2
#Questão 3
def repete_texto(texto,n):
    """Função que repete n vezes o texto de entrada. Str, int -> str"""
    msg = texto*n
    return msg
#Questão 4
def data(dia,mes,ano):
    """Função que retorna uma sequência de caracteres em formato de data DD/MM/AAAA
    Exemplo: data(24,5,1992)
    int,int,int -> str"""
    var_data = str(dia)+'/'+str(mes)+'/'+str(ano)
    return var_data
#Questão 5
def comportamento(x):
    """Função que retorna o comportamento de uma função matemática. int ou float -> int ou float."""
    if x <= 2:
        y = x
    elif 2 < x <= 3.5:
        y = 2
    elif 3.5 < x <= 5.5:
        y = 3
    else:
        y = x**2-10*x+28
    return y
#Questão 6
def desconto_inss(salariobruto):
    """Função que calcula o desconto de imposto de INSS de acordo com a tabela. int ou float -> float"""
    if salariobruto <= 2000:
        desconto = 0.06*salariobruto
    elif salariobruto <= 3000:
        desconto = 0.08*salariobruto
    else:
        desconto = 0.10*salariobruto
    return desconto
def desconto_ir(salariobruto):
    """Função que calcula a taxa de desconto de IR de acordo com a tabela do IR. int ou float -> float"""
    if salariobruto <= 2500:
        desconto = 0.11*salariobruto
    elif salariobruto <= 5000:
        desconto = 0.15*salariobruto
    else:
        desconto = 0.22*salariobruto
    return desconto
def salario_liquido(salariobruto):
    """Função que calcula e retorna o salário líquido de um funcionário trabalhista descontando INSS e IR. int ou float -> float"""
    descontos = desconto_inss(salariobruto) + desconto_ir(salariobruto)
    return salariobruto - descontos
