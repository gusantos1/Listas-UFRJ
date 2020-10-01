#Questão 1
def siga(tupla):
    """Função que retorna uma tupla com a Aprovação ou não do aluno.
    Use tupla: ('Nome_do_aluno',nota1,nota2,nota3)
    tupla -> tupla"""
    media = round((tupla[1]+tupla[2]+tupla[3])/3,2)
    if media >= 7:
        return (tupla[0],media,'Aprovado','Parabéns!')
    elif 5 <= media < 7:
        return (tupla[0], media, 'Aprovado')
    else:
        return (tupla[0], media, 'Reprovado')
#Questão 2
from math import degrees
def quadrante(angulo,graus=True):
    """Função que retorna o quadrante de um ângulo no círculo trigonométrico.
    Use angulo: int ou float.
    Use graus: True, se o valor do parâmetro angulo  for em graus.
    Use graus: False, se o valor do parâmetro angulo for em radianos.
    int ou float, bool -> int"""
    #método degrees converte diretamente radianos p/ graus.
    if graus == False:
        angulo = degrees(angulo)
    if 0 <= angulo%360 <= 90:
        return 1
    elif angulo%360 <= 180:
        return 2
    elif angulo%360 <= 270:
        return 3
    else:
        return 4
