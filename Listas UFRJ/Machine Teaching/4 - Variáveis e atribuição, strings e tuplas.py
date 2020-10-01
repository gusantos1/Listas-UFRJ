#Questão - Hashtag
def hashtag(s):
    """Função que insere o caractere # no início, meio e no final de uma string.
    str -> str"""
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio:] + '#'
#Questão - Filtragem
def filtra_pares(tupla):
    """Função que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla apenas com os elementos pares da tupla original.
    Use tupla: (elemento1,elemento2,elemento3,elemento4).
    tupla -> tupla"""
    pares = []
    for elemento in tupla:
        if elemento%2==0:
            pares.append(elemento)
    return tuple(pares)
#Questão - Número de dias
def diff_datas(data1,data2):
    """Função que retorna o calculo total de dias passados entre uma data e outra.
    Use o formato ”DD/MM/AAAA” para data1 e data2. str,str -> int"""
    data1 = int(data1[:2])+int(data1[3:5])*30+int(data1[6:])*365
    data2 = int(data2[:2])+int(data2[3:5])*30+int(data2[6:])*365
    var_dif_datas = data2 - data1
    return var_dif_datas
#Questão - Substituição
def substitui(s,x,i):
    """Função que recebe duas strings e subistuí um caracter pelo número de entrada.
    str,str,int -> str
    Use s: String
    Use x: Caracter que substituirá
    Use i: Inteiro entre 0 e o comprimento da String"""
    #Não usar o método replace, pois irá substituir todos os elementos
    s = list(s)
    s[i] = x
    nova_string = ''.join(s)
    return nova_string
#Questão - String recursiva
def recursiva(s):
    """Função que recebe uma string e retorna essa string no meio dela mesma.
    str -> str"""
    meio = len(s) // 2
    return s[:meio] + s + s[meio:]
#Questão - Concatenação
def concatenacao(a, b):
    """Função que retornar a concatenação de duas strings.
    str,str -> str
    Use arg1: Primeira String
    Use arg2: Segunda string"""
    return a+b+b+a
#Questão - Detectando colisões com tuplas
def colisao(ret1,ret2):
    """a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
tuple, tuple --> bool"""
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if not (x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and not (y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2):
        return True
    else:
        return False
