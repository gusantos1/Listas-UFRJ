#Questão 1
def concatenar(arg1,arg2):
    """Função que retornar a concatenação de duas strings.
    str,str -> str
    Use arg1: Primeira String
    Use arg2: Segunda string"""
    return arg1+arg2+arg2+arg1
#Questão 2
def num_sorte(nome,idade):
    """Função que retorna o número da sorte de uma pessoa.
    str,int -> float
    Use nome: Nome da pessoa ('Guilherme')
    Use idade: Idade da pessoa"""
    sorte = (((((idade*4)+8)*60)/240)+22)-idade
    return f'Parabéns, {nome}! Seu número da sorte é {sorte}!'
#Questão 3
def concatena15(string1, string2):
    string1 = string1[5:]
    string2 = string2[:-10]
    return string1, string2,
#Questão 4
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
#Questão 5
def recursiva(s):
    """Função que recebe uma string e retorna essa string no meio dela mesma.
    str -> str"""
    meio = len(s) // 2
    return s[:meio] + s + s[meio:]
#Questão 6
def string_meio_fim(string, caractere):
    """Função que insere um caractere no início, meio e no final de uma string.
    str,str -> str"""
    meio = len(string)//2
    return caractere + string[:meio] + caractere + string[meio:] + caractere
#Questão 7
def string_tres_esq(string):
    """Função que rotaciona 3 posições de uma string para esquerda e retorna sua concatenação.
    Assuma que a sting passada tenha no mínimo 3 caracteres.
    str -> str"""
    return string[-3:]+string[:-3]
#Questão 8
def copia(string,i):
    """Função que recebe uma string e um inteiro maior ou igual o tamanho da string e rotaciona a string x posições para a esquerda.
    str, int -> str"""
    return string[i:]+string[:i]
#Questão 9
def copia_if(string,i):
    """Função que recebe uma string e um inteiro (independente do tamanho da string) e rotaciona a string x posições para a esquerda.
    str, int -> str """
    if i < len(string):
        return string
    else:
        return string[i:]+string[:i]
#Questão 10
def data(data1,data2):
    """Função que retorna o total de dias passada entre uma data e outra.
    Considere a segunda data sendo maior que a primeira e que todos os mês possuem 30dias.
    str, str -> int"""
    dias_1 = int(data1[0:2])+int(data1[3:5])*30+int(data1[6:])*365
    dias_2 = int(data2[0:2])+int(data2[3:5])*30+int(data2[6:])*365
    return dias_2-dias_1
#Questão 11
def colisao(ret1,ret2):
    """a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
tuple, tuple --> bool"""
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if not (x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and not (y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2):
        return True
    else:
        return False