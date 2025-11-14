name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovei = float(input("Digite a nota do filme:\n"))

print("\nDADOS DO FILME:")
print("===========================")
# Alternativa 1
#print("Nome do filme:",name)
#print("Ano do filme:",yearLaunch)
#print("Nota do filme:",noteMovei)

# Alternativa 2 - Tudo em um print só.
#print("Nome do filme:",name,"\nAno de lançamento",yearLaunch,"\nNota do filme:",noteMovei)

# Alternativa 3 - Utilizando fstring.
print(f"Nome do filme: {name}\n"
      f"Ano de lançamento: {yearLaunch}\n"
      f"Nota do filme: {noteMovei}"
      )
print("Outro Novembro.")
print("Outro Dezembro.")
print("Novo Janeiro.")



