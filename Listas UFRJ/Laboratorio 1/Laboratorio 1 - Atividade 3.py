#Questão 1
def absoluto(arg):
    """Função que retorna o valor absoluto de um número. int,float -> int,float"""
    return abs(arg)
#Questão 2
def quantidade_raizes(a,b,c):
    """Função que retorna a quantidade de raízes de uma função do 2ª grau. int,float => int"""
    delta = b**2-4*a*c
    if delta < 0:
        return 0
    elif delta == 0:
        return 1
    else:
        return 2
#Questão 3
def seq_palavra(arg):
    """Função que retorna uma sequência de caracteres. str -> str"""
    return arg+arg+arg
#Questão 4
def comportamento(x):
    """Função que retorna o comportamento de uma função matemática. int ou float -> int ou float."""
    if x <= 2:
        y = x
    elif x <= 3.5:
        y = 2
    elif x <= 5.5:
        y = 3
    else:
        y = x**2-10*x+28
    return y
#Questão 5
comportamento(1)
comportamento(6)
#Questão 6
def meia_entrada(idade,carteira):
    """Função que retorna o direito de meia-entrada. int,bool -> str"""
    if idade >= 65 or idade <= 21 or carteira == True:
        return 'Tem direito a meia entrada.'
    else:
        return 'Não tem direito a meia entrada.'
#Questão 7
def classificacao(cv,ce,cs,fv,fe,fs):
    """Função que retorna o resultado de um campeonato entre Cormengo e Flaminthians.
    Use cv: Número de vitórias de Cormengo
    Use ce: Número de empates de Cormengo
    Use cs: Saldo de gols de Cormengo
    Use fv: Número de vitórias de Flaminthians
    Use fe: Número de empates de FLaminthians
    Use fs: Saldo de gols de Flaminthians
    Saída: Int -> Str"""
    cormengo = cv * 3 + ce
    flaminthians = fv * 3 + fe
    if cormengo == flaminthians:
        if cs == fs:
            return 'Empate'
        else:
            if cs > fs:
                return 'Cormengo'
            else:
                return 'Flaminthians'
    else:
        if cormengo > flaminthians:
            return 'Cormengo'
        else:
            return 'Flaminthians'
#Questão 8
def avioes(Competidores,QuantidadePapel,QuantidadeFolhas):
    """Função que retorna 'Suficiente' ou 'Insuficiente' conforme a quantidade comprada.
    Use Competidores: Quantidade de competidores
    Use QuantidadePapel: Quantidade de papéis comprados
    Use QuantidadeFolhas: Quantidade de papéis distrubuídos para os competidores
    Saída: Int -> Str"""
    folhas_real = Competidores*QuantidadeFolhas
    if folhas_real <= QuantidadePapel:
        return 'Suficiente'
    else:
        return 'Insuficiente'
