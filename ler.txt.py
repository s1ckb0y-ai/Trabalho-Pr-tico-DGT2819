arquivo = open("fsociety.txt", "r", encoding="utf-8")

conteudo = arquivo.read()
print("Conteúdo completo do arquivo:\n")
print(conteudo)

arquivo.close()

arquivo = open("fsociety.txt", "r", encoding="utf-8")
primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:\n")
print(primeira_linha)

arquivo.close()

arquivo = open("fsociety.txt", "r", encoding="utf-8")
tres_primeiros = arquivo.read(3)
print("\nOs 3 primeiros caracteres do arquivo:\n")
print(tres_primeiros)

arquivo.close()

print("\nLeitura com with:\n")
with open("fsociety.txt", "r", encoding="utf-8") as arquivo:
    conteudo_with = arquivo.read()
    print(conteudo_with)