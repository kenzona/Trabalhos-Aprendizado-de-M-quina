def erm(X, y, G, loss):
    melhor_g = None
    menor_risco = float("inf")

    for beta, g in G:
        risco = sum(
            loss(yi, g(xi))
            for xi, yi in zip(X, y)
        ) / len(X)

        if risco < menor_risco:
            menor_risco = risco
            melhor_g = (beta, g)

    return melhor_g, menor_risco


def loss_l2(y, y_hat):
    return (y - y_hat) ** 2


def loss_l1(y, y_hat):
    return abs(y - y_hat)


# Dados
X = [1, 2, 3, 4]
y = [3, 4, 8, 10]


# Classe de funções
G = []

for i in range(51):
    beta = i / 10
    g = lambda x, beta=beta: beta * x

    G.append((beta, g))


# L2
(melhor_beta_l2, g_l2), risco_l2 = erm(
    X, y, G, loss_l2
)


# L1
(melhor_beta_l1, g_l1), risco_l1 = erm(
    X, y, G, loss_l1
)


print("L2")
print("Melhor beta:", melhor_beta_l2)
print("Risco:", risco_l2)

print()

print("L1")
print("Melhor beta:", melhor_beta_l1)
print("Risco:", risco_l1)