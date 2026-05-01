lista_frutas = ["Morango", "Maçã", "Uva"]

#lista_frutas[0] = "Morango"
#lista_frutas[1] = "Maçã"
#lista_frutas[2] = "Uva"
print(lista_frutas[1])

lista_frutas.append("Melancia")
print(lista_frutas[3])
print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

for fruta in lista_frutas:
    print(fruta)
    print()
    print()

duplas = ["Ana", "Maria", "Vini", "Nat"]

for i in range(len(duplas)):
    for j in range(i + 1, len(duplas)):
        print(f"possiveis duplas: {duplas[i]} e {duplas[j]}")


# ----------------------------------------------------------
# 1. A LISTA
# ----------------------------------------------------------

# Uma lista guarda vários valores em uma única variável.
# Cada item ocupa uma posição chamada ÍNDICE, começando em 0.

# duplas = ["Ana", "Maria", "Vini", "Nat"]
#índice:    0       1       2      3


# ----------------------------------------------------------
# 2. len() — conta quantos itens existem na lista
# ----------------------------------------------------------

# len é abreviação de "length" (comprimento em inglês).
# Ele olha para dentro da lista e devolve o total de elementos.

# print(len(duplas))      # → 4  (há 4 nomes)
# print(len("hello"))     # → 5  (há 5 letras)
# print(len([10, 20, 30]))# → 3  (há 3 números)


# ----------------------------------------------------------
# 3. range() — gera uma sequência de números inteiros
# ----------------------------------------------------------

# ⚠️  O número FINAL nunca é incluído — o range para um passo antes.

# Forma 1: range(n)        → de 0 até n-1
# Forma 2: range(i, n)     → de i até n-1
# Forma 3: range(i, n, p)  → de i até n-1, pulando de p em p

# list(range(4))          # → [0, 1, 2, 3]
# list(range(1, 4))       # → [1, 2, 3]
# list(range(0, 10, 2))   # → [0, 2, 4, 6, 8]

# # Combinando len() e range():
# # range(len(duplas)) → range(4) → gera 0, 1, 2, 3
# # Isso significa: "repita o loop uma vez para cada índice da lista"
#
#
# # ----------------------------------------------------------
# # 4. O CÓDIGO PRINCIPAL — gerando todas as duplas possíveis
# # ----------------------------------------------------------
#
# duplas = ["Ana", "Maria", "Vini", "Nat"]
#
# # Loop externo: i percorre todos os índices da lista (0, 1, 2, 3)
# for i in range(len(duplas)):
#
#     # Loop interno: j começa SEMPRE em i+1, nunca antes.
#     #
#     # Isso serve para duas coisas:
#     #   ✅ Evitar que alguém forme dupla consigo mesmo (ex: Ana e Ana)
#     #   ✅ Evitar pares repetidos (ex: Ana+Maria e Maria+Ana seriam a mesma dupla)
#     #
#     # Evolução de j a cada rodada de i:
#     #   i=0 (Ana)   → range(1, 4) → j assume 1, 2, 3
#     #   i=1 (Maria) → range(2, 4) → j assume 2, 3
#     #   i=2 (Vini)  → range(3, 4) → j assume 3
#     #   i=3 (Nat)   → range(4, 4) → vazio, não executa nada
#
#     for j in range(i + 1, len(duplas)):
#
#         # f-string: forma moderna de montar textos com variáveis.
#         # Tudo dentro de {} é substituído pelo valor da variável.
#         print(f"possiveis duplas: {duplas[i]} e {duplas[j]}")
#
#
# # ----------------------------------------------------------
# # 5. SAÍDA ESPERADA
# # ----------------------------------------------------------
#
# # possiveis duplas: Ana e Maria
# # possiveis duplas: Ana e Vini
# # possiveis duplas: Ana e Nat
# # possiveis duplas: Maria e Vini
# # possiveis duplas: Maria e Nat
# # possiveis duplas: Vini e Nat
#
# # Total: 6 duplas únicas.
# # Isso corresponde à fórmula matemática de combinação: C(4,2) = 6
# # C(n, k) = n! / (k! * (n - k)!)  →  4! / (2! * 2!) = 24 / 4 = 6
#
#
# # ----------------------------------------------------------
# # 6. RESUMO RÁPIDO PARA CONSULTA
# # ----------------------------------------------------------
#
# # | Recurso            | O que faz                              | Exemplo                        |
# # |--------------------|----------------------------------------|--------------------------------|
# # | len(lista)         | Conta os elementos                     | len(["A","B","C"]) → 3         |
# # | range(n)           | Sequência de 0 até n-1                 | range(3) → 0, 1, 2             |
# # | range(i, n)        | Sequência de i até n-1                 | range(1, 3) → 1, 2             |
# # | range(i, n, passo) | Sequência de i até n-1 pulando         | range(0, 6, 2) → 0, 2, 4      |
# # | for i in range()   | Repete o bloco para cada número gerado | —                              |
# # | lista[i]           | Acessa o item no índice i              | duplas[0] → "Ana"              |
# # | f"texto {var}"     | Monta string com variável dentro       | f"Olá {nome}" → "Olá Ana"      |


