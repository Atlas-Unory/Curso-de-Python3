# Filtro de dados em listcomprehension

import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produtos = [
    {"nome": "p1", "preco": 20},
    {"nome": "p2", "preco": 10},
    {"nome": "p3", "preco": 30}
]

novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.50}
    if produto["preco"] > 20 else {**produto}
    for produto in produtos
    if (produto["preco"]) >= 20 and produto["preco"] * 1.50 > 10
]


# lista = [n for n in range(10) if n < 5]

p(novos_produtos)
