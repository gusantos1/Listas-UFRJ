#Questão 1
def area_retangulo(base,altura):
    """Função que retorna a área de um retângulo. Entrada: int ou float. Saída: int ou float."""
    return base*altura
#Questão 2
def area_da_superficie_cubo(c):
    """Função que retorna a área da superfície de um cubo. Entrada: int ou float. Saída: int ou float.
    C representa o valor da aresta."""
    return (c**2)*6
#Questão 3
def area_coroa_circular(r1,r2):
    """Função que retorna a área da da coroa circular. Entrada: int ou float. Saída: int ou float."""
    pi = 3.14
    area = pi*((r1 ** 2) - (r2 ** 2))
    return area
#Questão 4
def media_dois_numeros(arg1,arg2):
    """Função que retorna o valor da média entre dois números. Entrada: int ou float. Saída: int ou float."""
    media = (arg1+arg2)/2
    return media
#Questão 5
def funcao_segundo_grau(a,b,c,abscissa):
    """Função que retorna o valor da ordenada de uma função de segundo grau. Entrada: int ou float. Saída: int ou float."""
    y = a*(abscissa*abscissa)+(b*abscissa)+c
    return y
#Questão 6
def media_ponderada(peso1,nota1,peso2,nota2):
    """Função que retorna o valor da média ponderada de dois números. Entrada: int ou float. Saída: int ou float.
    Use a ordem de entradas como: Peso 1, Nota 1, Peso 2, Nota 2."""
    media_pon = ((peso1*nota1)+(peso2*nota2))/(peso1+peso2)
    return media_pon
#Questão 7
def erro_de_aproximacao_pg(n,r):
    """calcula a diferença entre a soma infinita de uma pg de razão (r) e a somatória parcial dado o número de termos (n) int,float->float """
    return 1/(1-r)-((r**n)-1)/(r-1)
#Questão 8
def gorjeta(valor):
    """Função que retorna o valor da gorjeta considerando 10% do valor da conta. Entrada: int ou float. Saída: int ou float."""
    return valor*0.1
#Questão 9
def gorjeta_e_porcentagem(valor,porc_gorjeta):
    """Função que retorna o valor da gorjeta considerando 10% do valor da conta. Entrada: int ou float. Saída: int ou float.
    Para porcentagem da gorjeta, use o valor sem aplicar a porcentagem. Se a porcentagem for igual a 20%, use 20"""
    return valor*(porc_gorjeta/100)
#Questão 10
def juros_simples(saldo_inicial,meses,juros):
    """Função que retorna o saldo final de uma conta com base nos juros simples. Entrada: int ou float. Saída: int ou float.
    Para os juros, use o valor sem aplicar a porcentagem. Se juros for igual a 1.2%, use 1.2"""
    juros = juros/100
    saldo_final = saldo_inicial*(1+(juros*meses))
    return saldo_final
#Questão 11
def distancia(vel_correnteza,largura_rio,vel_barco):
    """Função que calcula a distância que a correnteza arrasta um barco que atravessa um rio. Entrada: int ou float. Saída: int ou float"""
    return (largura_rio/vel_barco)*vel_correnteza
