#Questão 1
def area_retangulo(base, altura):
    """Função que retorna a área de um retângulo. int ou float -> int ou float
    base: base do retângulo
    altura: altura do retângulo"""
    return base * altura
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
    """Função que retorna o resto e a divisão de uma operação. int ou float -> int ou float.
    Use num1: Qualquer valor entre os reais.
    Use num2: Qualquer valor entre os reais, exceto 0."""
    divisao = num1 / num2
    resto = num1 % num2
    return resto, round(divisao, 2)
#Questão 4
def funcao_segundo_grau(a,b,c,abscissa):
    """Função que retorna o valor da ordenada de um polinômio do segundo grau. int,int,int,int -> int ou float
    Use a: Um valor diferente de 0.
    Use b, c e abscissa: Valores entre os reais."""
    return a*abscissa**2+b*abscissa+c
#Questão 5
def gorjeta(valor):
    """Função que retorna o valor de uma gorjeta que vale 10% do valor da conta. int ou float -> float
    Use valor: valor da conta."""
    return valor*0.1
#Questão 6
def media_dois_numeros(num1,num2):
    """Função que retorna a média entre dois números. int ou float - > int ou float
    Use num1: um valor entre os reais.
    Use num2: um valor entre os reais."""
    return (num1+num2) / 2
#Questão 7
def media_ponderada(peso1,nota1,peso2,nota2):
    """Função que retorna a média ponderada entre duas notas. int ou float - > float
    Use peso1: Peso da primeira nota.
    Use nota1: Valor da primeira nota.
    Use peso2: Peso da segunda nota.
    Use nota2: valor da segunda nota."""
    return ((peso1*nota1) + (peso2*nota2)) / (peso1+peso2)
#Questão 8
def distancia(vel_correnteza,largura_rio,vel_barco):
    """Função que retorna a distância que a correnteza arrasta um barco. int ou float -> float
    Use vel_correnteza: Valor para a velocidade da correnteza.
    Use largura_rio: Valor para a largura do rio.
    Use vel_barco: Valor para a velocidade do barco."""
    return (largura_rio/vel_barco) * vel_correnteza
#Questão 9
def juros_simples(saldo_inicial,meses,juros):
    """Função que retorna o saldo final de uma conta. int ou float, int, int ou float -> float
    Use saldo_inicial: Valor do saldo inicial da conta.
    Use meses: Valor referente aos meses.
    Use juros: valor referente aos juros."""
    return saldo_inicial*(1+((juros/100)*meses))
#Questão 10
def erro_soma_pg(n,q):
    """Função que retorna o erro do valor da soma de uma PG inifita. int,int -> float
    Use n: Quantidade de termos.
    Use q: Valor da razão. """
    return (1/(1-q))-(((q**n)-1)/(q-1))
#Questão 11
def maratona(partida,chegada):
    """Função que retorna o tempo total de um corredor de maratona em horas, minutos e segundos. tuple -> tuple
    Use partida: Tempo de partida.
    Use chegada: Tempo de chegada."""
    tempo_chegada = chegada[0]*3600 + chegada[1]*60 + chegada[2]
    tempo_partida = partida[0]*3600 + partida[1]*60 + partida[2]
    tempo_total = abs(tempo_chegada - tempo_partida)
    if tempo_total >= 3600:
        return tempo_total // 3600, (tempo_total % 3600)//60, ((tempo_total % 3600) % 60)
    elif tempo_total >= 60:
        return (tempo_total % 3600)//60, ((tempo_total % 3600) % 60)
    else:
        return (tempo_total % 3600) % 6

    # UMA FORMA MAIS SIMPLES DE RESOLVER A QUESTÃO.
    # from datetime import datetime
    # def maratona_datetime(tempo_partida, tempo_chegada):
    #     partida = datetime.strptime(tempo_partida, '%H:%M:%S')
    #     chegada = datetime.strptime(tempo_chegada, '%H:%M:%S')
    #     return chegada - partida


#Questão 12
def rachar_conta(valor,pessoas):
    """Função que retorna o valor a ser pago num restaurante. int ou float, int -> int ou float.
    Use valor: Valor da conta do restaurante.
    Use pessoas: Valor de pessoas que irão participar."""
    total = (valor*1.10) / pessoas
    return round(total, 2)
#Questão 13
def area_da_superficie_cubo(c):
    """Função que retorna a área do cubo com base na aresta. int ou float -> int ou float"""
    return c**2 * 6

if __name__ == '__main__':
    def enunciado(valor):
        print(f'\nQUESTÃO {valor}')
    #Questão 1
    enunciado(1)
    print(area_retangulo(5, 7))
    print(area_retangulo(15, 2))
    print(area_retangulo(500, 700))
    # Questão 2
    enunciado(2)
    print(area_coroa_circular(2, 1))
    print(area_coroa_circular(15, 5))
    print(area_coroa_circular(100, 0))
    # Questão 3
    enunciado(3)
    print(resto_divisao(10, 2))
    print(resto_divisao(8, 6))
    print(resto_divisao(9, 3))
    # Questão 4
    enunciado(4)
    print(funcao_segundo_grau(1, 4, 5, 2))
    # Questão 5
    enunciado(5)
    print(gorjeta(120))
    # Questão 6
    enunciado(6)
    print(media_dois_numeros(-5, 7))
    print(media_dois_numeros(2, -2))
    print(media_dois_numeros(5, 5))
    print(media_dois_numeros(3, 4))
    print(media_dois_numeros(3.0, 4.0))
    # Questão 7
    enunciado(7)
    print(media_ponderada(10, 10, 10, 10))
    print(media_ponderada(10, 2, 10, 3.5))
    # Questão 8
    enunciado(8)
    print(distancia(4,10,2))
    # Questão 9
    enunciado(9)
    print(juros_simples(600, 15, 3))
    # Questão 10
    enunciado(10)
    print(erro_soma_pg(2, 0))
    print(erro_soma_pg(3, 0.5))
    # Questão 11
    enunciado(11)
    print(maratona((5, 0, 0), (6, 0, 10)))
    print(maratona((4, 15, 17), (5, 23, 45)))
    print(maratona((22, 0, 0), (23, 23, 45)))
    # Questão 12
    enunciado(12)
    print(rachar_conta(100,2))
    # Questão 13
    enunciado(13)
    print(area_da_superficie_cubo(5))
