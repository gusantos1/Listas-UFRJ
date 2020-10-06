#Questão 1 - Filtra múltiplos
def filtraMultiplos(*listan):
    """Função que recebe uma lista com uma lista de valores e um inteiro (n) e retorna outra lista com os valores divisíveis por n.
    use list[list,int] -> list: [[24, 15, 3, 8], 2] -> [24,8] """
    valores_lista = listan[0]
    inteiro = listan[1]
    divisiveis = []
    contador = 0
    while contador < len(valores_lista):
        if valores_lista[contador] % inteiro == 0:
            divisiveis.append(valores_lista[contador])
        contador+=1
    return divisiveis
    # for filtrar in valores_lista:
    #     if filtrar%inteiro == 0:
    #         divisiveis.append(filtrar)
    # return divisiveis
#Questão 2 - Consoantes em maiúsculas
def uppCons(frase):
    """Função que recebe uma string e retorna a string com todas as consoantes em maísculas.
    use str -> str : ['Um homem que podia tudo!'] -> UM HoMeM Que PoDia TuDo!"""
    contador = 0
    #A questão não está considerando 'v' como consoante.
    while contador < len(frase):
        if frase[contador] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtWwXxZzç':
            frase = frase.replace(frase[contador],frase[contador].upper())
        contador += 1
    return frase
#Questão 3 - Posição da Letra
def posLetra(string, letra, o):
    """Função que recebe uma string, uma letra e um número que indica a ocorrência desejada e retorna em que posição da string a ocorrência da letra está.
    Caso exista menos ocorrências da letra do que  a ocorrência pedida, a função retorna -1.
    Use str, str, int -> ("mariana come banana", 'a', 3) -> int"""
    #Em que indice está a o° letra ?
    indice = ocorrencia = 0
    #Estrutura de repetição.
    while indice < len(string):
        #Condicional para cada letra da frase com o parâmetro (letra) da função e somando + 1 se for true..
        if string[indice] == letra:
            ocorrencia+=1
            #Condicional para o contador de ocorrência com o parâmetro (o) da função e retornando o index da letra.
            if ocorrencia == o:
                return string.index(string[indice], indice)
        indice+=1
    else:
        return -1
#Questão 4 - Repetidos
def repetidos(lista):
    """Função que recebe uma lista de números como entrada e retorna o número de vezes que um elemento da lista é igual ao anterior.
            Use list -> int: [22, 22, 6, 5, 5, 28, 28] - > 3 """
    anterior = atual = contador = vezes = 0
    # Estrutura de repetição.
    while contador < len(lista):
        # Condicional inicial oara o primeiro número.
        if contador == 0:
            atual = lista[contador]
        # Condicional para os números com índices maiores que 0.
        else:
            atual = lista[contador]
            if anterior == atual:
                vezes += 1
        anterior = atual
        contador += 1
    return vezes
#Questão 5 - Fatorial
def fatorial(num):
    """Função que recebe um número e retorna o fatorial. Use int -> int: 5 -> 120"""
    c = cont = 1
    while cont < num:
        cont += 1
        c *= cont
    return c
    # c = 1
    # for x in range(1,num+1):
    #     c*=x
    # return c
#Questão 6 - Peça Perdida
def faltante(lista):
    """Função que recebe uma lista com N-1 inteiro e retorna o número inteiro deste intervalo.
    Use list -> int: [1, 2, 3, 5] -> 4"""
    contador = 1
    resultado = 0
    #Estrutura de repetição e condicional.
    while contador <= len(lista):
        if contador not in lista:
            resultado += contador
        contador = lista[contador-1]+1
    #Condicional que completa a lista crescente com o sucessor do último valor.
    if resultado == 0:
        resultado += len(lista)+1
    return resultado
