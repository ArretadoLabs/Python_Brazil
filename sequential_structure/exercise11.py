"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
one = int(input())
two = int(input())
three = float(input())
operation_one = (one * 2) * (two / 2)
operation_two = (one * 3) + three
operation_three = (three ** 2)
print("operation one: %.2f " % operation_one)
print("operation two: %.2f " % operation_two)
print("operation three: %.2f " % operation_three)
