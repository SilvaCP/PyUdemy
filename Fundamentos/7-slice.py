# String[inicio:fim] - índice começa na posição 0 | índice final -1
moveiName = "Top Gun"
# Busca toda a String apartir da primeira posição.
print(moveiName[0:])
"""
String[início:fim:passo]
índice começa na posição 0 | índice final -1
passo - determina o incremento. Por padrão esse número é o 1.
"""
# Buscar toda a string de 2 em 2 caracteres.
print(moveiName[::2])
# Buscar toda a string nos índeces ímpares.
print(moveiName[1::2])
# Inverter uma string de trás para frente.
print(moveiName[::-1])
