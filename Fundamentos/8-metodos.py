moveiName = "Top Gun"
moveiDescription = """
    Top Gun Maverick, é um filme de avaliação e aventura,
    Muito consagrado
na indústria.
"""
"""
print(moveiName.upper()) # Tudo em maiúsculo.
print(moveiName.lower()) # Tudo em minúsculo.
print(moveiName.capitalize()) # A primeira letra em maiúscula.
print(moveiName.title()) # A primeira letra de cada palavra em maiúscula.
print(moveiName.center) # Centralizado com preenchimento.
print(moveiName.find("u")) # Busca por posição do caractere.
print(moveiName.find("o")) # Também conta caracteres.
print(moveiName.replace("Top","Matrix")) # Altera elemento por outro.
print(moveiDescription.split(',')) # Separa por vírgula.
"""
"""
Exercício 5 - Operações em Strings
Objetivo:
Reforçar operações em Strings.

Escreva um programa que leia uma palavra e um número inteiro n.
O programa deve:
    Imprimir a palavra duas vezes concatenada (sem espaço).
    Imprimir a palavra repetida n vezes (usando multiplicação de string).
Exemplo
Entrada:
Python
3
Saída:
PythonPython
PythonPythonPython
"""
palavra = input("Digite uma palavra qualquer:")
numero = int(input("Informe um número inteiro qualquer entre 2 a 6:"))
print(palavra * 2)
print(numero * palavra)


