import numpy as np


def lagrange(xs, ys):
    """
    Recebe os pontos xs e ys e retorna uma função p(x)
    que avalia o polinômio interpolador de Lagrange.
    """

    n = len(xs)

    def p(x):
        resultado = 0.0

        for i in range(n):

            # Calcula L_i(x)
            Li = 1.0

            for j in range(n):
                if i != j:
                    Li *= (x - xs[j]) / (xs[i] - xs[j])

            resultado += ys[i] * Li

        return resultado

    return p


# ---------------------------------------
# (a) Pontos e função verdadeira
# ---------------------------------------

xs = np.linspace(-1, 1, 10)

def f(x):
    return np.sin(3 * x)


# Ponto onde vamos avaliar o interpolador
x0 = 0.95


# ---------------------------------------
# (b) Uma realização do experimento
# ---------------------------------------

eps = np.random.normal(
    loc=0,
    scale=0.1,
    size=10
)

ys = f(xs) + eps

p = lagrange(xs, ys)

print("Uma realização:")
print("p(x0) =", p(x0))
print("f(x0) =", f(x0))


# ---------------------------------------
# (c) Repetir 100 vezes
# ---------------------------------------

valores = []

for _ in range(100):

    # Reamostra apenas o ruído
    eps = np.random.normal(
        loc=0,
        scale=0.1,
        size=10
    )

    # Mantém xs fixos
    ys = f(xs) + eps

    # Novo interpolador
    p = lagrange(xs, ys)

    # Avalia no mesmo x0
    valores.append(p(x0))


media = np.mean(valores)

desvio_padrao = np.std(
    valores,
    ddof=1
)


# ---------------------------------------
# Resultados
# ---------------------------------------

print("\nApós 100 repetições:")

print("Média de p(x0):", media)

print("Desvio padrão de p(x0):", desvio_padrao)

print("f(x0):", f(x0))