from math import *
#Questão 1.
def media(valor1, valor2, valor3, valor4):
    """Função que retorna a média de quatro números inteiros. int,int,int,int -> int"""
    var_media = (valor1 + valor2 + valor3 + valor4) / 4
    return var_media
def bombons(dinheiro,preco):
    """Função que retorna a quantidade de bombons possíveis para compra. int ou float -> int
    Use dinheiro: Valor referente ao dinheiro.
    Use preço: Valor referente ao preço."""
    return dinheiro//preco
#Questão 2
def hip_triangulo_retangulo(coposto,cadjacente):
    """Função que retorna a hipotenusa de um triângulo retângulo. int ou float -> int ou float
    Use coposto: Valor do cateto oposto.
    Use cadjacente: Valor do cateto adjacente."""
    return hypot(coposto,cadjacente)
def distancia(xaya,xbyb):
    """Função que calcula a distância entre dois pontos.
    [xa,ya],[xb,yb] -> list -> float"""
    resultado = dist(xaya, xbyb)
    return resultado
    # Outra alternativa para o resultado.
    # return sqrt((xbyb[0]-xaya[0])**2+(xbyb[1]-xaya[1])**2)
def perimetro(caoposto,cadjacente):
    """Função que retorna o perímetro de um triângulo retângulo. int ou float -> int ou flaot
    Use coposto: Valor do cateto oposto.
    Use cadjacente: Valor do cateto adjacente."""
    return caoposto+cadjacente+hip_triangulo_retangulo(caoposto,cadjacente)
def somas(arg1,arg2):
    """Função que retorna a soma do quadrado do seno com o quadrado do cosseno de um ângulo. int -> float
    Use arg1: Valor referente ao seno.
    Use arg2: Valor referente ao cosseno."""
    return (sin(radians(arg1)))**2+(cos(radians(arg2)))**2
#Questão 3
def comprimento_circulo(r):
    """Função que retorna o comprimento de um círculo. int ou float -> float.
    Use r: Valor referente ao raio."""
    return 2*pi*r
#Questão 4
def pista_circular(r,dis):
    """Função que retorna o número de voltas que um atleta percorreu. int ou float -> float
    Use r: Valor referente ao raio.
    Use dis: Valor referente a distância."""
    return round(dis / comprimento_circulo(r),1)
#Questão 5
def delta(a,b,c):
    """Função que retorna do discriminante de uma função do segundo grau. int,int,int -> int"""
    return b**2-4*a*c
def primeira_raiz(a,b,c):
    """Função que retorna o valor da primeira raiz real de uma função do segundo grau. int,int,int -> int"""
    return (-b+sqrt(delta(a,b,c)))/(2*a)
def segunda_raiz(a,b,c):
    """Função que retorna o valor da segunda raiz real de uma função do segundo grau. int,int,int -> int"""
    return (-b-sqrt(delta(a,b,c)))/(2*a)
#Questão 6
def area_setor_circular(r,alfa=360):
    """Função que retorna o valor da área do setor circular. int ou float -> float
    Use r: Valor referente ao raio.
    Use alfa: Valor referente ao alfa, o padrão é 360°"""
    return 3.14*alfa*r**2/360
#Questão 7
def posicao_do_termo(a1,an,r):
    """Função que calcula a posição do termo. int,int,int -> int"""
    posicao_n = (an-a1)+1/r
    return posicao_n
def soma_da_pa(a1,an,r):
    """Função que calcula a soma de uma PA. int,int,int -> float"""
    soma_pa = ((a1+an)*(posicao_do_termo(a1,an,r)))/2
    return soma_pa
#Questão 8
def bolo(farinha,ovo,leite):
    """Função que retorna a quantidade máxima de bolos. int,int,int -> int"""
    farinha=trunc(farinha/2)
    ovo=trunc(ovo/3)
    leite=trunc(leite/5)
    resultado = min(farinha,ovo,leite)
    return resultado
