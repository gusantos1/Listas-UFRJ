#Questão 1 - Quantidade de palavras
def quant_palavras(frase):
    """Função que recebe uma string e retorna o número de palavras da frase desconsiderando os espaços. str -> int"""
    frase = frase.split()
    return len(frase)
#Questão 2 - Conta frases
def conta_frases(texto):
    """Função que recebe um texto e retorna o número de frases dentro dele. str -> int"""
    especias = ['!','?','.']
    texto = texto.split()
    contador = 0
    for laco_palavras in texto:
        for laco_especiais in especias:
            if laco_especiais in laco_palavras:
                contador+=1
    return contador
#Questão 3 - Intercalando listas
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    nova_lista = [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return nova_lista
    #Usando o método zip
    # nova_lista = zip(lista1,lista2)
    # nova_lista = list(nova_lista)
    # vazia = []
    # for x in nova_lista:
    #     for y in x:
    #         vazia.append(y)
    # return vazia
#Questão 4 - Retira pontuacao
def retira_pontuacao(frase):
    """Função que recebe uma frase e substitui todas as pontuações por espaço. str -> str"""
    especias = ['!', '?', '#', '$', '@', '%', '&', '*', ',', '.', '-']
    for trocar in especias:
        frase = frase.replace(trocar,' ')
    return frase
#Questão 5 - De trás pra frente
def inverte(string):
    """Função que recebe uma string e retorna a mesma de modo invertido. str -> str"""
    string = string.lower()
    especias = ['!','?','#','$','@','%','&','*',',','.','-']
    for testar in especias:
        if testar != '-' and testar in string:
            string = string.replace(testar,'')
        else:
            string = string.replace(testar,' ')
    string = string.split()
    string.reverse()
    string = ' '.join(string)
    return string
#Questão 6 - Pirâmide de números
def piramide_num(num1,num2):
    """Função que retorna uma pirâmidade de números inteiros dados dois números. int,int -> list.
    Use num1: Valor referente ao primeiro número.
    Use num2: Valor referente ao segundo número."""
    lista = []
    if num1 >= 0 and num2 > 0 or num1 > 0 and num2 < 0 or num1 < 0 and num2 < 0 or num1 < 0 and num2 > 0:
        if num1 > num2:
            for var_laco in range(num1,num2,-1):
                lista.append(var_laco)
            for var_laco in range(num2,num1+1):
                lista.append(var_laco)
        else:
            for var_laco in range(num1,num2):
                lista.append(var_laco)
            for var_laco in range(num2,num1-1,-1):
                lista.append(var_laco)
    return lista
#Questão 7 - Colchão
def colchao(medidas,h,l):
    """Função que retorna um valor booleano pra saber se um colchão de medidas a,b,c passa por uma porta de medidas h,l.
    list,int,int -> bool
    Use medidas: Medidas do colchão em ordem crescente.
    Use h: Altura da portão
    Use l: Larguda da porta"""
    #Medidas do colchão
    a,b,c = medidas[0],medidas[1],medidas[2]
    #Encontrar o menor lado do colchão para o menor lado da porta
    primeiro_menor_lado_colchao = min(a,b,c)
    #Encontrar o segundo menor lado do colcão para o segundo menor lado da porta
    lista_segundo_lado_colchao = []
    if primeiro_menor_lado_colchao != a:
        lista_segundo_lado_colchao.append(a)
    elif primeiro_menor_lado_colchao != b:
        lista_segundo_lado_colchao.append(b)
    else:
        lista_segundo_lado_colchao.append(c)
    segundo_menor_lado_colchao = min(lista_segundo_lado_colchao)
    #Condição que vai comparar os lados do colchão com as medidas da porta.
    if primeiro_menor_lado_colchao <= l and segundo_menor_lado_colchao <= h:
        return True
    else:
        return False