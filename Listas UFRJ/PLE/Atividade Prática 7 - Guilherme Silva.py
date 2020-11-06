#Questão 1 - Dados
from random import randint
def dados():
    """Função que simula um jogo de dois dados. Não há parâmetros."""
    vezes_jogadas = 0
    while True:
        dado1, dado2 = randint(1, 6), randint(1, 6)
        vezes_jogadas += 1
        if dado1 == dado2:
            return vezes_jogadas
#Questão 2 - contatinhosApp
def buscar(lista=list,nome=str):
    """Função que recebe uma lista com N usuários cadastrato e o nome de um usuário da lista e retorna uma lista com as informações do(s) usuário(s) referente ao nome usado como parâmetro.
    use list, str -> list"""
    i = 0
    retorno = []
    #Estrutura de repetição para identificar os usuários com o parâmetro (nome).
    while i < len(lista):
        if nome.capitalize() in lista[i][0]:
            retorno.append(lista[i])
        i += 1
    else:
        return retorno
a = [ ['Bruno Fields',['2199112233','2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields',['2198145233'], '', '@juju.fields']]
print(buscar(a,'bruno'))

