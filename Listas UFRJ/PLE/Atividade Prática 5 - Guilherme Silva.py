def zodiaco(ano):
    """Função que recebe o ano de uma pessoa e retorna seu signo no zodíaco chinês. int - > str
    Use ano: Valor referente ao ano de nascimento."""
    var_ano = ano%12
    signos = [0,'Macaco',1,'Galo',2,'Cão',3,'Porco',4,'Rato',5,'Boi',6,'Tigre',7,'Coelho',8,'Dragão',9,'Serpente',10,'Cavalo',11,'Carneiro']
    for x in signos:
        while x == var_ano:
            return signos[signos.index(x)+1]