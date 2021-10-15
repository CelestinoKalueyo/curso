"""Altere o programa anterior permitindo ao usuário informar
as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação."""


popA = float(input("Digite a população do país A: "))
popB = float(input("Digite a população do país B: "))
anos = 0
taxa_crescimentoA = float(input("informe a taxa de crescimento da população da cidade A: "))
taxa_crescimentoB = float(input("informe a taxa de crescimento da população da cidade B: "))
while popA < popB:
	popA += round((popA*taxa_crescimentoA)/100)
	popB += round((popB*taxa_crescimentoB)/100)
	anos += 1

print("levará",anos,"anos para população da cidade A ser maior que a cidade B")
print("populaçãoB:",popB,"habitantes")
print("populaçãoA:", popA,"habitantes")