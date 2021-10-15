"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

print("="*30)
nome = str(input("Digite o seu nome: "))
while (len(nome) <= 3):
    nome = str(input("Digite o seu nome: "))


idade = int(input("Digite a sua idade: "))
while (idade > 150 or idade < 0):
    idade = int(input("Digite a sua idade: "))


salario = float(input("Digite o seu salário: "))
while (salario < 0):
    salario = float(input("Digite o seu salário: "))


sexo = str(input("Digite o seu sexo: "))
while sexo != "f" and sexo != "m":
    sexo = str(input("Digite o seu sexo: "))


estado_civil = str(input("Digite o seu estado civil:"))
while (estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
    estado_civil = str(input("Digite o seu estado civil:"))
print("="*30)