#Questão 1.A
from math import pi
def somatorio(termo):
    """Função que calcula o somatório da série com n = 0 tendendo ao infinito de (-1)**n/2*n+1.
    Use n: referente a termo."""
    cont_somatorio = 0
    for n in range(0, termo+1):
        var_somatrio = ((-1)**n)/(2*n+1)
        cont_somatorio += var_somatrio
    return cont_somatorio
#Questão 1.B
def somatorio_erro():
    """Função que calcula a soma da série com erro inferior a 0,01, de modo que |Sn-pi/4| < 0.01.
    Retorna uma tupla com o número de termos necessários para chegar ao erro e o somatório do termo referente ao erro.
    Função sem parâmetros."""
    cont = 0
    #Solução com uso do For.
    for achar_erro in range(0, 99999):
        if abs(somatorio(achar_erro) - pi/4) < 0.01:
            break
        cont += 1
    return cont, somatorio(cont)

    # #Solução com uso do While que melhor se adequa a questão..
    # cont = 0
    # while abs(somatorio(cont) - pi / 4) > 0.01:
    #     cont += 1
    # return cont, somatorio(cont)

#Questão 2 - ContatinhoAPP (For)
def buscar(lista=list,nome=str):
    """Função que recebe uma lista com N usuários cadastrato e o nome de um usuário da lista e retorna uma lista com as informações do(s) usuário(s) referente ao nome usado como parâmetro.
    use list, str -> list"""
    retorno = []
    for achar in range(0, len(lista)):
        if nome.capitalize() in lista[achar][0]:
            retorno.append(lista[achar])
    return retorno
