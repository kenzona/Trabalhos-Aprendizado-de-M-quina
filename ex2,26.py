import numpy as np


# ============================================================
# 1. FUNÇÃO VERDADEIRA
# ============================================================

def f(x):
    return np.sin(2 * np.pi * x)


# ============================================================
# 2. kNN
# ============================================================

def knn_predict(X_treino, y_treino, x, k):
    """
    Faz uma previsão kNN para um único ponto x.
    """

    # Distâncias entre x e todos os pontos de treinamento
    distancias = np.abs(X_treino - x)

    # Índices dos k vizinhos mais próximos
    indices = np.argsort(distancias)[:k]

    # Previsão = média dos valores dos k vizinhos
    return np.mean(y_treino[indices])


# ============================================================
# 3. PARÂMETROS DO EXPERIMENTO
# ============================================================

np.random.seed(42)

N = 50
n_repeticoes = 200

x0 = 0.3
variancia_ruido = 0.1
desvio_ruido = np.sqrt(variancia_ruido)

valores_k = [1, 3, 10, 30, 50]

# Valor verdadeiro de f(x0)
valor_verdadeiro = f(x0)

print("=" * 65)
print("SIMULAÇÃO DE VIÉS E VARIÂNCIA DO kNN")
print("=" * 65)

print(f"f(x0) = f({x0}) = {valor_verdadeiro:.6f}")
print(f"Var(ε) = {variancia_ruido}")
print(f"N = {N}")
print(f"Repetições = {n_repeticoes}")

print()


# ============================================================
# 4. EXPERIMENTO PARA CADA k
# ============================================================

for k in valores_k:

    previsoes = []

    # --------------------------------------------------------
    # Repetimos o experimento 200 vezes
    # --------------------------------------------------------

    for repeticao in range(n_repeticoes):

        # ----------------------------------------------------
        # Gera os pontos X de treinamento
        # ----------------------------------------------------

        X_treino = np.random.uniform(0, 1, N)

        # ----------------------------------------------------
        # Gera o ruído
        #
        # ε ~ N(0, 0.1)
        # ----------------------------------------------------

        epsilon = np.random.normal(
            loc=0,
            scale=desvio_ruido,
            size=N
        )

        # ----------------------------------------------------
        # Gera as observações:
        #
        # y = f(x) + ε
        # ----------------------------------------------------

        y_treino = f(X_treino) + epsilon

        # ----------------------------------------------------
        # Treina implicitamente o kNN e calcula
        # a previsão em x0
        # ----------------------------------------------------

        previsao = knn_predict(
            X_treino,
            y_treino,
            x0,
            k
        )

        previsoes.append(previsao)

    # Converte para NumPy
    previsoes = np.array(previsoes)

    # ========================================================
    # 5. ESTIMATIVA DO VALOR ESPERADO
    # ========================================================

    media_previsoes = np.mean(previsoes)

    # ========================================================
    # 6. VIÉS AO QUADRADO
    #
    # (f(x0) - E[f^(x0)])²
    # ========================================================

    vies_quadrado = (
        valor_verdadeiro - media_previsoes
    ) ** 2

    # ========================================================
    # 7. VARIÂNCIA
    #
    # Var(f^(x0))
    # ========================================================

    variancia = np.var(previsoes)

    # ========================================================
    # 8. RESULTADOS
    # ========================================================

    print("-" * 65)

    print(f"k = {k}")

    print(
        f"E[f^(x0)]          = {media_previsoes:.6f}"
    )

    print(
        f"Viés²               = {vies_quadrado:.6f}"
    )

    print(
        f"Variância           = {variancia:.6f}"
    )

    print(
        f"Erro total estimado = "
        f"{vies_quadrado + variancia:.6f}"
    )