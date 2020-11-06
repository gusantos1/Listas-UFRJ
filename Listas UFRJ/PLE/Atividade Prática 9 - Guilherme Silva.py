#Questão1. "Quem ligou" ContatinhosApp
def quem_ligou(lista,telefone):
    """Função que recebe um número de telefone e retorna o contato referente ao número.
    str or int -> list"""
    telefone = str(telefone)
    resultado = []
    for usuario in lista:
        for telefones in usuario[1]:
            if telefone in telefones:
                resultado.append(usuario)
    return resultado
