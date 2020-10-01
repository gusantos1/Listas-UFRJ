#Questão - Futebol
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
#Questão - Positivo, Negativo ou Zero?
def PosNegZero(x):
    """Função que recebe um inteiro e retorna se é maior, igual ou menor que 0. int - > str"""
    if x < 0:
        return str(x)+' e negativo'
    elif x == 0:
        return str(x)+' e zero'
    else:
        return str(x)+' e positivo'
#Questão - Aviões de Papel
def avioes(c, p_compr, p_compet):
    """Função que retorna 'Suficiente' ou 'Insuficiente' conforme a quantidade comprada.
    Use c: Quantidade de competidores
    Use p_compr: Quantidade de papéis comprados
    Use p_compet: Quantidade de papéis distrubuídos para os competidores
    Saída: Int -> Str"""
    folhas_real = c * p_compet
    if folhas_real <= p_compr:
        return 'Suficiente'
    else:
        return 'Insuficiente'
