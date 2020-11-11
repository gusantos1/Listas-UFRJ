from math import *
#Questão 1.A
print(max(3,2.8,3.9))
print(min(7,2,4,1,0))
#Questão 1.B
def media(arg1,arg2,arg3):
    """Função que retorna a média de três números inteiros. int -> float"""
    var_media = (arg1 + arg2 + arg3) / 3
    return var_media
#Questão 1.C
def media_max(arg1,arg2,arg3):
    """Função que retorna a diferença do maior deles com a média. int -> float"""
    var_max = max(arg1,arg2,arg3)
    return var_max-media(arg1,arg2,arg3)
#Questão 1.D
def media_min(arg1,arg2,arg3):
    """Função que retorna a diferença do menor deles com a média. int -> float"""
    var_min = min(arg1,arg2,arg3)
    return var_min-media(arg1,arg2,arg3)
#Questão 2.A
def delta(a,b,c):
    """Função que calcula o discriminante(delta). int -> int ou float"""
    return b**2-4*a*c
#Questão 2.B
def primeira_raiz(a,b,c):
    """Função que calcula o primeira raiz real da equação do segundo grau. int -> int ou float"""
    return (-b+sqrt(delta(a,b,c)))/(2*a)
#Questão 2.C
def segunda_raiz(a,b,c):
    """Função que calcula a segunda raiz real da equação do segundo grau. int -> int ou float"""
    return (-b-sqrt(delta(a,b,c)))/(2*a)
#Questão 3.A.B.C
def termo_geral(i,f,r):
    """Função que calcula o enésimo termo de uma PA. int -> int ou float"""
    enesimo = i+(f-1)*r
    return enesimo
def soma_da_pa(i,f,r):
    """Função que calcula a soma de uma PA. int -> float"""
    soma_pa = ((i+termo_geral(i,f,r))*f)/2
    return soma_pa
#Questão 4.A
def hip_triangulo_retangulo(coposto,cadjacente):
    """Função que calcula o valor da hipotenusa de um triângulo retângulo. int ou float -> float"""
    return hypot(coposto,cadjacente)
#Questão 4.B
def distancia(x1y1,x2y2):
    """Função que calcula a distância entre dois pontos de um plano cartesiano. Use entradas, como:
    [5.2],[2.0] -> 3.2 . float -> float"""
    resultado = dist(x1y1, x2y2)
    return resultado
#Questão 4.C
def perimetro(caoposto,cadjacente):
    """Função que calcula o perímetro de um triângulo reto. int ou float -> float"""
    return caoposto+cadjacente+hip_triangulo_retangulo(caoposto,cadjacente)
#Questão 4.D
def somas(arg,arg2):
    return sin(radians(arg))*2+cos(radians(arg2))*2
#Questão 4.E
def comprimento_circulo(r):
    """Função que calcula o comprimento do círculo. int -> float"""
    return 2*pi*r
#Questão 5
def area_setor_circular(r,alfa=360):
    """Função que calcula a área do setor circular. int ou float -> float"""
    return 3.14*alfa*r**2/360
#Questão 6
def bombons(dinheiro, preco):
    """Função que calcula a compra de bombons. int ou float -> int"""
    return trunc(dinheiro/preco)
#Questão 7
def imc(peso,altura):
    """Função que calcula o imc. int ou float -> float"""
    return round(peso/altura**2,2)
#Questão 8
def carros_viagem(pessoas,c=5):
    """Função que calcula a capacidade máxima do número de pessoas dentro de um veículo. int -> int"""
    return ceil(pessoas/c)
#Questão 9
def pista_circular(r,dis):
    """Função que retorna o número de voltas feita numa pista circular. int ou float -> float"""
    return round(dis - comprimento_circulo(r),1)
#Questão 10
def bolo(farinha,ovo,leite):
    """Função que a quantidade máxima de bolos. int -> int"""
    farinha=trunc(farinha/2)
    ovo=trunc(ovo/3)
    leite=trunc(leite/5)
    resultado = min(farinha,ovo,leite)
    return resultado
