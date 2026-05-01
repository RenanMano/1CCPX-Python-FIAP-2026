musicas = [
    ["This love", "Maroom 5"],
    ["Boate azul", "Bruno e Marrone"],
    ["Dormi na praça", "Leonardo"]
]

for musica in musicas:
    for info in musica:
        print(info)
    print()



# Lista aninhada: cada item da lista principal é também uma lista.
# Cada lista interna representa uma música no formato [nome, artista].
musicas = [
    ["This love",      "Maroon 5"],         # índice 0
    ["Boate azul",     "Bruno e Marrone"],  # índice 1
    ["Dormi na praça", "Leonardo"]          # índice 2
]

# Loop externo: a cada volta, "musica" recebe uma lista interna inteira.
# Ex: na primeira volta, musica = ["This love", "Maroon 5"]
for musica in musicas:

    # Loop interno: a cada volta, "info" recebe um item da lista interna.
    # Ex: primeira volta → info = "This love"
    #     segunda volta  → info = "Maroon 5"
    for info in musica:
        print(info)

    # print() sem argumentos imprime uma linha em branco.
    # Serve para separar visualmente cada música na saída.
    print()

# Saída esperada:
# This love
# Maroon 5
#
# Boate azul
# Bruno e Marrone
#
# Dormi na praça
# Leonardo