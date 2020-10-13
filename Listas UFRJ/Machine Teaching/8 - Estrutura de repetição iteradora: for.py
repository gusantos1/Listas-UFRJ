#Questão 1 - Soma de números ímpares
def soma_impar(n):
    """Função que recebe um inteiro e retorna a soma dos n primeiros números ímpares.int -> int"""
    cont = impares = 0
    for x in range(1, 999):
        if cont < n:
            if x % 2 != 0:
                impares += x
                cont += 1
    return impares
#Questão 2 - Soma fatorial
def soma_fatorial():
    """Função que calcula o fatorial dos números inteiros de 1 a 10. Sem entradas."""
    fat = contador = 1
    soma = 0
    for x in range(0, 10):
        for x in range(contador, contador+1):
            fat *= x
        contador += 1
        soma += fat
    return soma
#Questão 3 - Divisores
def divisores(n):
    """Função que recebe um inteiro e retorna o número de divisores inteiros possíveis. int -> int"""
    divis = 0
    for x in range(1, n+1):
        if n % x == 0:
            divis += 1
    return divis

#Questão 4 - Números primos
def primo(n):
    """Função que recebe um inteiro positivo e verifica se é primo ou não, retornando um valor booleano. int -> bool"""
    cont = 0
    for x in range(1, n+1):
        if n % x == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False
#Questão 5 - Soma H
def soma_h(n):
    """Função que recebe um inteiro e calcula a série harmônica de N."""
    soma = 0
    for x in range(1, n+1):
        soma += 1/x
    return round(soma, 2)
#Questão 6 - Soma Esquisita
from math import factorial
def soma():
    """Função que retorna a soma de frações decrescentes de origem: inteiro/fatorial, inteiros de 10 a 1 e fatorial de 1! a 10!.
    Sem parâmetros."""
    cont = 1
    soma = 0
    for x in range(10, -1, -1):
        if x % 2 == 0:
            soma += x/factorial(cont)
        else:
            soma -= x/factorial(cont)
        cont += 1
    return round(soma, 2)
#Questão 7 - Língua do P
def lingua_p(frase):
    """Função que recebe uma frase e retorna a mesma traduzida para a língua do P. str -> str"""
    frase = list(frase.lower())
    i = 0
    for x in frase:
        if x in 'ãaeéiou':
            concatenada = 'p'+x
            frase.insert(frase.index(x,i)+1,concatenada)
        i += 1
    copia = ''.join(frase)
    return copia
