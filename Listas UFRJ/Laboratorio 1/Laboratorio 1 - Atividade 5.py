#Questão 1
def analisando_string(frase):
    """Função que retorna o número de palavras da frase.
    str -> str"""
    var_frase = frase.strip()
    return len(var_frase.split())
#Questão 2
def nova_frase(frase,palavra,pos1,pos2):
    """Função que retorna a frase excluindo os ocorrências da palavra entre as posições 'pos1' e 'pos2'.
    str,str,int,int -> str"""
    retirando = palavra[pos1-1:pos2+1]
    nova_palavra = palavra.replace(retirando,'')
    nova_frase = frase.replace(palavra,nova_palavra)
    return nova_frase
#Questão 3
def substituir(frase):
    """Função que substitui todos os espaços em branco por '#'.
    str -> str"""
    frase = frase.split()
    nova_frase = '#'.join(frase)
    return nova_frase
#Questão 4
def novastring(string,caractere):
    """Função que retorna apenas o trecho da string situada entre a primeira ocorrência do caractere até o final da string.
    str,str -> str"""
    i = string.find(caractere)
    nova = string[i+1:]
    return nova
#Questão5
def tupla(*args):
    """Função que retorna duas tuplas, sendo a primeira apenas do tipo strings e a segunda apenas do tipo inteito,float ou complex.
    tuple -> tuple,tuple"""
    letras = []
    numeros = []
    if type(args[0]) is str:
        letras.append(args[0])
    else:
        numeros.append(args[0])
    if type(args[1]) is str:
        letras.append(args[1])
    else:
        numeros.append(args[1])
    if type(args[2]) is str:
        letras.append(args[2])
    else:
        numeros.append(args[2])
    return tuple(letras),tuple(numeros)
#Questão 6
def geradora_lista3(*args):
    """Função que gera uma lista a partir de duas e a ordena em ordem crescente. list -> list"""
    return sorted(args[0]+args[1])
