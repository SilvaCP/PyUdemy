"""
filmeList = [
    "Inception", "The Shawshank Redemption", "The Dark kgnith",
    "Pulp fiction", "Interstellar", "Big Hero"
]
# 1 - Tamanho da lista;
print(len(filmeList))

# 2 - Exemplo prático; Você tem uma lista de filmes na sua locadora, e quer saber queal é o código do filme pelo nome. Utilize o método .index;
print(filmeList.index("Interstellar"))

# 3 - Adicionando um item ao final da lista.
filmeList.append("The lord of the rings.")
print(filmeList)
print(len(filmeList)) # Tamanho da lista 7 contando com o 0.

# 4 - Ordenar list
filmeList.sort()
print(filmeList)

# 5 - Copiar os itens de uma lista para outra, e removendo um iten específico;
filmeCopy = filmeList.copy()
filmeCopy.remove("The lord of the rings.")
print(filmeCopy)

# 6 - Removendo todos os itens da lista.
filmeList.clear()
print(filmeList)

"""

n1 = int(input("Informe o 1º número: "))
n2 = int(input("Informe o 2º número: "))
n3 = int(input("Informe o 3º número: "))

listNumeros = [n1,n2,n3]

print(listNumeros)
print(listNumeros[0])
somaListNumeros = sum(listNumeros)
print(somaListNumeros)

