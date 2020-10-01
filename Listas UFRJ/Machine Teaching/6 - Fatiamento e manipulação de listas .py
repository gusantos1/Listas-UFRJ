#Questão 1 - Altera frase
def altera_frase(frase,palavra,i):
    """Função que recebe uma frase,u uma palavra e um número inteiro como posição para substituir em maiúscula a palavra na frase, caso ela já exista. str,str,int -> str"""
    frase_temp = frase.upper().split()
    if palavra.upper() in frase_temp:
        #encontrando índice da palavra e substituindo.
        achar = frase_temp.index(palavra.upper())
        frase = frase.split()
        frase[achar] = palavra.upper()
        frase = ' '.join(frase)
        return frase
    else:
        frase = frase.split()
        frase.insert(i,palavra)
        frase = ' '.join(frase)
        return frase
#Questão 2 - Faltas no campeonato
def faltas(args):
    """Função que retorna o total de faltas cometidas no campeonato.
    list -> int
    Use as entrada na lista, sequencialmente: [['Time','Adversário',[faltaTime,FaltaAdversário]
    Exemplo: [['Brasil','Italia', [10,9]],['Brasil','Espanha', [5,7]],['Italia','Espanha', [10,9]]"""
    nova = sum(args[0][2]+args[1][2]+args[2][2])
    return nova
#Questão 3 - Insere ordenado
def insere(lista_numero,n):
    """Função que acrescenta um número n numa lista crescente mantendo sua ordenação.
    Use lista_numero: lista crescente.
    Use n: valor referente ao número que será inserido.
    list,int -> list"""
    lista_numero.insert(0,n)
    return sorted(lista_numero)
#Questão 4 - Maiores
def maiores(*args):
    """Função que retorna uma lista com todos os elementos maiores que (n).
    Use list: list[list, int] -> list
    list -> list"""
    nova_lista = args[0]
    n = args[1]
    nova_lista.append(n)
    if max(nova_lista) == n:
        return []
    else:
        lista_decrescente = sorted(nova_lista, reverse=True)
        index_n = lista_decrescente.index(n)
        return sorted(lista_decrescente[:index_n])
#Questão 5 - Média da turma
def media(*notas):
    """Função que recebe uma lista com a as notas dos alunos e retorna a média e a as notas maiores que a média. list -> list"""
    media_notas = sum(notas[0])/len(notas[0])
    notas_maiores = []
    for maiores in notas[0]:
        if maiores > media_notas:
            notas_maiores.append(maiores)
    return media_notas, sorted(notas_maiores)
#Questão 6 - Ordenada?
def eh_ordenada(args):
    """"Função que recebe uma lista com valores numéricos e verefica se está ordenada retornando True ou False e a forma: crescente, decrescente ou desordenada. list -> tupla"""
    lista = args
    lista_temp = lista.copy()
    if lista == sorted(lista_temp):
        return True,'crescente'
    elif lista == sorted(lista_temp,reverse=True):
        return True,'decrescente'
    else:
        return False,'desordenada'
