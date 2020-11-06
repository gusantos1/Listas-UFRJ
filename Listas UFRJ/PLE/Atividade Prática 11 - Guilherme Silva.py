#Questão 1
from random import sample
def gera_matriz():
    """Função que gera uma matriz 4x4 com pares de 1 a 8. Sem parâmetros -> str"""
    matriz = [x for x in range(1, 9)] * 2
    for posicao in range(1, 17):
        i = sample(matriz, 1)[0]
        print(i, end=' ')
        matriz.remove(i)
        if posicao % 4 == 0:
            print('\n')

#Questão 2
def main():
    #globais
    elementos_matriz = [x for x in range(1, 9)] * 2
    matriz = []
    jogadas = termina = 0
    def forma_matriz():
        """Função que estrutura a matriz 4x4 cobrindo-a com '*' e
        acrescenta False referente ao par ainda não encontrado.
        Estrutura: [valor_sample,'*',False]. Sem parâmetros de entrada."""
        lista_temp = []
        for linha in range(0, 4):
            for coluna in range(1, 5):
                elemento_sorteado = sample(elementos_matriz, 1)[0]
                lista_temp.append(elemento_sorteado)
                elementos_matriz.remove(elemento_sorteado) #removendo o elemento repetido para que sobre apenas o que vai completar o par.
                lista_temp.append('*')
                lista_temp.append(False)
                if coluna % 4 == 0:
                    matriz.append(lista_temp)
                    lista_temp = []
    forma_matriz()
    def show_lista_matriz(lista_matriz):
        """Função que mostra a matriz 4x4. list -> str"""
        for lista in lista_matriz:
            for c in lista:
                if lista.index(c) == 1 or lista.index(c) == 4 or lista.index(c) == 7 or lista.index(c) == 10:
                    print(c, end=' ')
            print('\n')
    show_lista_matriz(matriz)
    while True:
        #Input 1: Configura e chama.
        def formata_primeira():
            """Função que recebe as coordenadas referente a primeira escolha e configura as saídas para int.
            Use: [valor_linha,valor_coluna] -> [0,2] .Elemento localizado na linha 0, coluna 3
            str -> int.int"""
            while True:
                escolha_primeira = input(f'Escolha a primeira posição[x,y]: ')
                if len(escolha_primeira) > 1:
                    escolha_primeira = escolha_primeira.replace('[', '')
                    escolha_primeira = escolha_primeira.replace(']', '')
                    escolha_primeira = escolha_primeira.replace(',', '')
                    x1, y1 = int(escolha_primeira[0]), int(escolha_primeira[1])
                    if x1 <= 3 and y1 <= 3 and matriz[x1][y1*3+2] is False: #matriz[x1][y1*3+2] representa se o valor já foi sorteado.
                        matriz[x1][y1*3 + 1] = str(matriz[x1][y1*3])
                        show_lista_matriz(matriz)
                        return x1, y1*3
                    else:
                        print('Opção inválida.', end=' ')
                else:
                    print('Opção inválida.', end=' ')
        x1, y1 = formata_primeira()
        #Input 2: Configura e chama.
        def formata_segunda():
            """Função que recebe as coordenadas referente a segunda escolha e configura as saídas para int.
            Use: [valor_linha,valor_coluna] -> [2,1] .Elemento localizado na linha 2, coluna 1
            str -> int.int"""
            while True:
                escolha_segunda = input(f'Escolha a segunda posição[x,y]: ')
                if len(escolha_segunda) > 1:
                    escolha_segunda = escolha_segunda.replace('[', '')
                    escolha_segunda = escolha_segunda.replace(']', '')
                    escolha_segunda = escolha_segunda.replace(',', '')
                    x2, y2 = int(escolha_segunda[0]), int(escolha_segunda[1])
                    foi_clicado_segundo = matriz[x2][y2*3+2]
                    if x2 <= 3 and y2 <= 3 and foi_clicado_segundo is False:
                        matriz[x2][y2*3+1] = str(matriz[x2][y2*3])
                        show_lista_matriz(matriz)
                        return x2, y2*3
                    else:
                        print('Opção inválida.', end=' ')
                else:
                    print('Opção inválida.', end=' ')
        x2, y2 = formata_segunda()
        # Mostra e vefifica rodada.
        def verifica_rodada():
            """Função que verifica se os valores escolhidos foram pares. Sem parâmetros -> str,int"""
            if matriz[x1][y1] != matriz[x2][y2]:
                print('Você errou... tente de novo.')
                matriz[x1][y1 + 1] = '*'
                matriz[x2][y2 + 1] = '*'
                show_lista_matriz(matriz)
                return 0
            else:
                print('Parabéns você acertou')
                matriz[x1][y1 + 2] = True
                matriz[x2][y2 + 2] = True
                return 1
        termina += verifica_rodada()
        jogadas += 1
        if termina == 8:
            print(f'Parabéns!! Você conseguiu descobrir todas as casas com {jogadas} jogadas!')
            break
if __name__ == '__main__':
    main()
