"""
Elabore um programa que leia um número que o usuário digitar. Dependendo do
número informado, das frases abaixo, o sistema imprimirá somente as que forem
verdadeiras.
○ O número é menor que 10.
○ O número é par.
○ O número está entre 8 e 16.
○ O número é 51 ou 80.
"""
print('-=-=-=-=-=-=-=-=PROVA DA GAMA-=-=-=-=-=-=-=-=')

numero = 0
numero = int(input("Digite um número: "))
if numero < 10:
    print("O número é menor que 10")
if numero % 2 == 0:
    print("O número é par")
if numero >= 8 and numero <= 16:
    print("O número está entre 8 e 16")
if numero == 51 or numero == 80:
    print("O número é 51 ou 80")