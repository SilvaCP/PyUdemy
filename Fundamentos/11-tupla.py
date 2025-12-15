'''
filmeTuple = (
    "Inception", "The Shawshank Redemption", "The Dark kgnith",
    "Pulp fiction", "Interstellar", "Big Hero"
    )

print(type(filmeTuple))

# 1 - Buscar os dois primeiros itens da tupla.
print(filmeTuple[:2])

# 2 - Buscar o último item da tupla.
print(filmeTuple[-1])

# 3 - Buscar filmes até uma determinada posição.
print(filmeTuple[:3])

# 4 - Buscar filmes de uma posição em diante.
print(filmeTuple[3:])

# 5 - Recuperar um item da tupla pelo nome.
print(filmeTuple.index("Big Hero"))

'''




# EXECÍCIO 7 - TUPLA.
'''
Escreva um programa que:

    Crie uma tupla com os nomes de três cidades lidas pelo usuário.

    Imprima:

        A tupla completa.

        O último elemento da tupla.

        A quantidade de elementos da tupla.
'''

cidadesTuple = ("Recife","Salvador","Fortaleza")
print(cidadesTuple)
print(cidadesTuple[-1])
print(len(cidadesTuple))