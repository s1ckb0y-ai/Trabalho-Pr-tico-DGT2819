arquivo = open("texto.txt", "w", encoding="utf-8")

texto = list()
texto.append("Python é uma linguagem versátil.\n")
texto.append("Este arquivo foi criado pelo script.\n")
texto.append("Estamos aprendendo leitura e escrita de arquivos.\n")

arquivo.writelines(texto)
arquivo.close()

print("Arquivo texto.txt criado com sucesso.")