def cadastro(nome,telefone='',email='',instagram=''):
    """Função que recebe 4 dados pessoais de um usuário e retorna uma lista contendo suas informações.
    Use nome: nome referente ao usuário.
    Use telefone: número de telefone referente ao usuário.
    Use email: email referente ao usuário.
    Use instagram: instagram referente ao usuário.
    str,str,str,str -> list"""
    dados =[nome,[telefone],email,instagram]
    return dados

def atualizar(lista,i=int,nova=str):
    """Função que atualiza os dados de um usuário no contatinhosAPP.
    Use lista: lista no formato de [nome,[telefone],email,instragram].
    Use i: valor referente ao índice que deseja a alteração.
    Use nova: valor referente a nova informação.
    list,int,str -> list"""
    #Condição de índices permitidos
    if 0 <= i <= 3:
        #Tratamento de dados exceto telefone.
        if i != 1:
            if i == 0:
                lista.insert(0,nova)
                lista.pop(1)
                return True
            elif i == 2:
                lista.insert(2,nova)
                lista.pop(3)
                return True
            elif i == 3:
                lista.insert(3,nova)
                lista.pop(4)
                return True
        #tratamento de dados apenas sobre telefone.
        else:
            if nova in lista[1]:
                lista.pop(1)
                return True
            else:
                lista[1].extend([nova])
                return True
