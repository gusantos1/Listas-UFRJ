#Questão 1
def frase_reverse(frase):
    """Função que retorna a inversão da frase como parâmetro. str -> str"""
    frase = frase.split()
    frase.reverse()
    nova_frase = ' '.join(frase)
    return nova_frase
#Questão 2
def frase_ordem(frase):
    """Função que retorna a frase reordenando-a em ordem alfabética. str -> str"""
    frase = frase.split()
    frase.sort()
    nova_frase =' '.join(frase)
    return nova_frase
#Questão 3
def trocar_por_i(frase):
    if 'a' in frase:
        frase = frase.replace('a','i')
    if 'e' in frase:
        frase = frase.replace('e','i')
    if 'o' in frase:
        frase = frase.replace('o','i')
    if 'u' in frase:
        frase = frase.replace('u','i')
    return frase
#Questão 4
def gerador_nova_frase(frase,palavra,posicao):
    if palavra in frase:
        nova_frase = frase.replace(palavra,palavra.upper())
        return nova_frase
    else:
        frase = frase.split()
        frase.insert(posicao,palavra)
        nova_frase = ' '.join(frase)
        return nova_frase
#Questão 5
def faltas_campeonato(args):
    """Função que retorna o total de faltas cometidas no campeonato.
    list -> int
    Use as entrada na lista, sequencialmente: [['Time','Adversário',[faltaTime,FaltaAdversário]
    Exemplo: ['Brasil','Italia', [10,9]],['Brasil','Espanha', [5,7]],['Italia','Espanha', [10,9]]]"""
    nova = sum(args[0][2]+args[1][2]+args[2][2])
    return nova
#Questão 6
def ordenada(args):
    """Função que ordena uma lista e inclue um número (n) posição correta da lista. list,int -> list"""
    nova_lista = args
    n = args[-1]
    nova_lista.append(n)
    return sorted(nova_lista)
#Questão 7
def decrescente(args):
    """Função que retorna uma lista com todos os elementos maiores que (n). list, int -> list"""
    nova_lista = args
    n = args[-1]
    nova_lista.append(n)
    lista_decrescente = sorted(nova_lista,reverse=True)
    return lista_decrescente[:n]
#Questão 8
def maior_da_lista(lista):
    """Função que retorna o maior elemento da lista. list > int ou float."""
    return max(lista)
#Questão 9
def media_alunos(lista_media):
    """Função que retorna a média da turma e uma lista com as notas que ficaram acima da média. list -> float, list"""
    nota = sum(lista_media)/len(lista_media)
    lista_media.sort()
    i = lista_media.index(7)
    maiores_notas = lista_media[i:]
    return f'Média dos alunos {round(nota,1)}, {maiores_notas}'

#Questão 10
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