#Questão 1
def ocorrencia():
    """Função que retorna o número de ocorrências de séries de faces repetidas de um dado. int -> int"""
    serie = input('Digite sua série: ')
    lista = list(serie)
    dentro = []
    repeticao = False
    for i in range(1,len(lista)):
        if lista[i] == lista[i-1] and repeticao == False:
            repeticao = True
            dentro.append(lista[i])
        else:
            repeticao = False
    return len(dentro)
#Questão2
def programa(i,a,b,c):
    """Função que lê um código i em um intervalo de 1 a 4, e 3 valores de a,b,c inteiros positivos com a<b, onde cada valor de i representa uma funcionalidade.
    int,int,int,int -> int ou float"""
    def trapezio(base_maior,base_menor,altura):
        """função que calcula a área do trapézio. int, int, int -> int ou float
        Use base_maior: parâmetro referente a maior base de um trapézio.
        Use base_menor: parâmetro referente a menor base de um trapézio.
        Use altura: parâmetro referente a altura de um trapézio."""
        return ((base_maior+base_menor)*altura)/2
    def quadrados(a,b,c):
        """Função que retorna os valores quadrados de 3 parâmetros. int,int,int -> int"""
        valor = [a**2, b**2, c**2]
        for mostrar in valor:
            print(mostrar, end=' ')
        return ''
    def media(a,b,c):
        """Função que retorna a média aritmética entre 3 parâmetros. int,int,int -> int ou float."""
        return round(sum([a,b,c])/3,2)
    def step(a,b,c):
        """Função que retorna a soma dos inteiros de a até b, usando c como variação(step). int,int,int -> int"""
        cont_soma = 0
        for soma in range(a,b,c):
            cont_soma += soma
        return cont_soma
    if i == 1:
        print(f'Função Área do trapézio.\nBase maior: {b}\nBase menor: {a}\nAltura: {c}\nResultado : ', end='')
        return trapezio(b,a,c)
    elif i == 2:
        print(f'Função que calcula: a x a, b x b, c x c.\na: {a}\nb: {b}\nc: {c}\nResultado: ', end='')
        return quadrados(a,b,c)
    elif i == 3:
        print(f'Função Média Aritmética entre a,b e c:\na: {a}\nb: {b}\nc: {c}\nResultado: ', end='')
        return media(a,b,c)
    else:
        print(f'Função que calcula a soma de 3 inteiros de a até b, usando c como variação.\n'
              f'a: {a}\nb: {b}\nc: {c}\nResultado: ', end='')
        return step(a,b,c)
#Questão 3
def busca(matriz=list, setor=str):
    """Função que recebe um setor como string e uma matriz e retorna os funcionários que atuam no parâmetro 'setor'.
    str, list -> list"""
    funcionarios = []
    for lista_funcionario in matriz:
        if setor.title() in str(lista_funcionario[2]).title():
            funcionario_copia = lista_funcionario.copy()
            del funcionario_copia[2]
            funcionarios.append(funcionario_copia)
    if len(funcionarios) == 0:
        print('Nenhum registro encontrado')
    else:
        print(funcionarios)
def main():
    import ast
    escolha = int(input(f'Escolha o modo que deseja inserir sua matriz:\n'
                        f'[1] De uma vez\n'
                        f'[2] Elemento por elemento\n'
                        f'Escolha: '))
    if escolha == 1:
        matriz = input('Digite sua matriz: ')
        matriz = ast.literal_eval(matriz)
    elif escolha == 2:
        matriz = []
        def add():
            nome = input('Nome do funcionário: ').strip().title()
            registro = input(f'Registro do {nome}: ')
            setor = input(f'Setor do {nome}: ').strip().title()
            telefone = input(f'Telefone do {nome}: ')
            return [nome,registro,setor,telefone]
        while True:
            matriz.append(add())
            continuar = input('Deseja continuar ? [S/N]').strip().upper()
            if continuar.startswith('N'):
                break
    setor = input('Digite o setor para busca: ').strip().title()
    return busca(matriz,setor)
