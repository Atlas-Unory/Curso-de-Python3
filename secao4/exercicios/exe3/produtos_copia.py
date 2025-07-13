# Solução - Proposta de 3 exercícios em um

from produtos import produtos
import copy

novos_produtos = [
    {**p, "preco": round(p["preco"] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

""" print(*produtos, sep="\n")
print()
print(*novos_produtos, sep="\n") """

produtos_ordenados_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p["nome"],
    reverse=True
)

produtos_ordenados_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p["preco"]
)

# Final
print(*produtos, sep="\n")
print()
print(*produtos_ordenados_nome, sep="\n")
print()
print(*produtos_ordenados_preco, sep="\n")
