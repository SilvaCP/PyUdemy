# ESTRUTURA DE DADOS - TIPO LISTA.
"""
# Lista recebe valores heterogênios.
filmeMatrix = ["Matrix", 1999, 8.7, True] # Valores passados como itens na lista.
print(type(filmeMatrix))  # <class 'list'>
print(filmeMatrix)
"""
filmeList = [
    "Inception", "The Shawshank Redemption", "The Dark kgnith",
    "Pulp fiction", "Interstellar", "Big Hero"
]
# 1 - Buscar os dois primeiros itens da lista;
print(filmeList[:2])
# 2 - Buscar o último iten da lista;
print(filmeList[-1])
# 3 - Buscar os três primeiros da lista;
print(filmeList[:3])
# 4 - Buscar filmes a partir de uma determinada possição até a terceira posição.
print(filmeList[1:4])
print(filmeList[2:4])
print(filmeList[3:4])




