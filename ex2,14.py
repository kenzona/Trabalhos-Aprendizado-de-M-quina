import math
import random


def knn_reg(X, y, x0, k):
    distancias = []

    # Calcula a distância entre x0 e cada ponto
    for xi, yi in zip(X, y):
        distancia = abs(xi - x0)
        distancias.append((distancia, yi))

    # Ordena pela distância
    distancias.sort()

    # Seleciona os k vizinhos mais próximos
    vizinhos = distancias[:k]

    # Calcula a média dos valores y
    soma = 0

    for distancia, yi in vizinhos:
        soma += yi

    return soma / k


# ----------------------------
# Geração dos dados
# ----------------------------

N = 100

X = []
y = []

for _ in range(N):
    x = random.uniform(0, 1)

    epsilon = random.uniform(-0.2, 0.2)

    yi = math.sin(2 * math.pi * x) + epsilon

    X.append(x)
    y.append(yi)


# ----------------------------
# Grade fina
# ----------------------------

grade = []

for i in range(1001):
    x0 = i / 1000
    grade.append(x0)


# ----------------------------
# Avaliação para diferentes k
# ----------------------------

ks = [1, 5, 20]

resultados = {}

for k in ks:
    previsoes = []

    for x0 in grade:
        y_hat = knn_reg(X, y, x0, k)
        previsoes.append(y_hat)

    resultados[k] = previsoes


# ----------------------------
# Mostrando algumas previsões
# ----------------------------

for k in ks:
    print(f"\nk = {k}")

    for i in range(0, len(grade), 100):
        print(
            f"x = {grade[i]:.2f}, "
            f"y_hat = {resultados[k][i]:.3f}"
        )