#moveiName = "Top Gun"
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
"""
palavra = input("Digite uma palavra qualquer:")
numero = int(input("Informe um número inteiro qualquer entre 2 a 6:"))
print(palavra * 2)
print(numero * palavra)
"""
# Ex1 -
"""
primeiroNome = input("Informe o primeiro nome: ")
segundoNome = input("Informe o sobrenome: ")
nomeFormatado = f"{primeiroNome} {segundoNome}"
print(nomeFormatado)
"""
# Ex2 - Inverter o texto.
"""
texto = "Python3 é interessante demais!"
palavras = texto.split()    # Transforma em itens de uma lista.
textoInvertido = " ".join(palavras[::-1])   # Concatema.
print(textoInvertido)
"""
# Ex3 - palindromo - diz-se de ou frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.

texto1 = "arara" 
texto2 = "python3"
texto3 = "ovo"
# Remove espaço e deixa nome em minúsculo.
texto1_format = texto1.lower().replace("", "")
texto2_format = texto2.lower().replace("", "")
texto3_format = texto3.lower().replace("", "")

# Verifique se o texto original é igual ao seu reverso.
palindromo1 = texto1_format == texto1[::-1]
palindromo2 = texto2_format == texto2[::-1]
palindromo3 = texto3_format == texto3[::-1]

# Saída esperada True ou False.
print(palindromo1)
print(palindromo2)
print(palindromo3)



