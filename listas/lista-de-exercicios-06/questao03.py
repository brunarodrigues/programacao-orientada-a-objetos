def copiando_arq (arq1, arq2):
    with open (arq1) as texto1:
        with open(arq2, "w") as texto2:
            for linha in texto1:
                if '//' not in linha:
                    print(linha,file = texto2)
copiando_arq("texto.txt","copia_texto.txt")
