"""Faça um programa que peça uma nota, entre zero e dez. Mostre
uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido."""


nota = 30
while 0 < nota > 10:
    nota = float(input("Digite a nota: "))
    if 0 < nota > 10:
        print("NOTA INVÁLIDA")
    else:
        print("NOTA VÁLIDA")







