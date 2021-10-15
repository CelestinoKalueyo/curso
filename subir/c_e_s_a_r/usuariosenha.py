"""Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário, mostrando uma mensagem
de erro e voltando a pedir as informações."""
nome = 0
senha = 0
while nome == senha:
    nome = str(input("Digite seu nome: "))
    senha = str(input("Digite sua senha: "))
    if nome == senha:
        print("ERRO")
    else:
        print("CORRETO")