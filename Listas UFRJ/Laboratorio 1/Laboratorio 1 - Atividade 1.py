#Questão 1
def area_retangulo(base,altura):
    """Função que retorna a área de um retângulo. Entrada: int ou float.int - > float"""
    return base*altura
#Questão 2
def area_coroa_circular(r1,r2):
    """Função que retorna a área da coroa circular. int ou float - > float
    Use r1: Raio de maior valor.
    Use r2: Raio de menor valor."""
    pi = 3.14
    area = pi*((r1 ** 2) - (r2 ** 2))
    return area
#Questão 3
def resto_divisao(num1,num2):
    """Função que retorna a divisão e o resto de uma operação. int ou float -> float,int
    Use num1: Um valor.
    Use num2: outro valor."""
    divisao = num1/num2
    resto = num1%num2
    return divisao,resto
#Questão 4
def funcao_segundo_grau(a,b,c,abscissa):
    """Função que retorna o valor de um polinômio do segundo grau.int,int,int,int -> int ou float
    Use a: valor > 0
    Use b: um valor.
    Use c: um valor.
    Use abscissa: um valor >=2"""
    y = a*(abscissa*abscissa)+(b*abscissa)+c
    return y
#Questão 5
def gorjeta(valor):
    """Função que retorna o valor de uma gorjeta que vale 10% do valor da conta. Use int ou float -> float"""
    return valor*0.1
#Questão 6
def media_dois_numeros(num1,num2):
    """Função que retorna a média entre dois números. int ou float - > int ou float
    Use num1: um valor.
    Use num2: outro valor."""
    media = (num1+num2)/2
    return media
#Questão 7
def media_ponderada(peso1,nota1,peso2,nota2):
    """Função que retorna a média ponderada entre duas notas. int ou float - > float
    Use peso1: Peso referente a primeira nota.
    Use nota1: Valor da primeira nota.
    Use peso2: Peso referente a segunda nota.
    Use nota2: valor da segunda nota."""
    media_pon = ((peso1*nota1)+(peso2*nota2))/(peso1+peso2)
    return media_pon
#Questão 8
def distancia(vel_correnteza,largura_rio,vel_barco):
    """Função que retorna a distância que a correnteza arrasta um barco. int ou float -> float
    Use vel_correnteza: Valor para a velocidade da correnteza.
    Use largura_rio: Valor para a largura do rio.
    Use vel_barco: Valor para a velocidade do barco."""
    return (largura_rio/vel_barco)*vel_correnteza
#Questão 9
def juros_simples(saldo_inicial,meses,juros):
    """Função que retorna o saldo final de uma conta. int ou float, int, int ou float -> float
    Use saldo_inicial: Valor do saldo inicial da conta.
    Use meses: Valor referente aos meses.
    Use juros: valor referente aos juros."""
    juros = juros/100
    saldo_final = saldo_inicial*(1+(juros*meses))
    return saldo_final
#Questão 10
def erro_soma_pg(n,q):
    """Função que retorna o erro do valor da soma de uma PG inifita. int,int -> float
    Use n: Valor do expoente da razão.
    Use q: Valor da razão. """
    return (1/(1-q))-(((q**n)-1)/(q-1))
#Questão 11
def maratona(partida,chegada):
    """Função que retorna o tempo total de um corredor de maratona em horas, minutos e segundos. tuple -> tuple
    Use partida: Tempo de partida.
    Use chegada: Tempo de chegada."""
    tempo_chegada = chegada[0]*3600+chegada[1]*60+chegada[2]
    tempo_partida = partida[0]*3600+partida[1]*60+partida[2]
    tempo_total = abs(tempo_chegada - tempo_partida)
    if tempo_total >= 3600:
        return tempo_total//3600, (tempo_total%3600)//60,((tempo_total%3600)%60)
    elif tempo_total >= 60:
        return (tempo_total%3600)//60,((tempo_total%3600)%60)
    else:
        return (tempo_total%3600)%60
#Questão 12
def rachar_conta(valor,pessoas):
    """Função que retorna o valor a ser pago num restaurante. int ou float, int -> int ou float.
    Use valor: Valor da conta do restaurante.
    Use pessoas: Valor de pessoas que irão participar."""
    total = (valor*1.10)/pessoas
    return round(total,2)
#Questão 13
def area_da_superficie_cubo(c):
    """Função que retorna a área do cubo com base na aresta. int ou float -> int ou float"""
    return c**2*6