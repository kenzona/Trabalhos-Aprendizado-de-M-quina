import numpy as np


# ============================================================
# 1. PARTIÇÃO DOS DADOS
# ============================================================

def particao_dados(X, y, k):
    """
    Divide os dados em k partes (folds).

    Retorna uma lista contendo os índices de cada fold.
    """

    n = len(X)

    # Embaralha os índices
    indices = np.random.permutation(n)

    # Divide os índices em k partes aproximadamente iguais
    folds = np.array_split(indices, k)

    return folds


# ============================================================
# 2. K-FOLD CROSS VALIDATION
# ============================================================

def k_fold(X, y, k, fit, predict, loss):
    """
    Realiza validação cruzada k-fold.

    Parâmetros:
        X       : dados de entrada
        y       : rótulos
        k       : número de folds
        fit     : função fit(X, y) -> modelo
        predict : função predict(modelo, X) -> previsões
        loss    : função loss(y_real, y_pred) -> erro

    Retorna:
        erro médio de validação cruzada.
    """

    folds = particao_dados(X, y, k)

    erros = []

    for i in range(k):

        # ----------------------------------------------------
        # Define os índices de teste
        # ----------------------------------------------------

        idx_teste = folds[i]

        # ----------------------------------------------------
        # Os outros folds serão usados para treinamento
        # ----------------------------------------------------

        idx_treino = np.concatenate(
            [folds[j] for j in range(k) if j != i]
        )

        # ----------------------------------------------------
        # Separa os dados
        # ----------------------------------------------------

        X_treino = X[idx_treino]
        y_treino = y[idx_treino]

        X_teste = X[idx_teste]
        y_teste = y[idx_teste]

        # ----------------------------------------------------
        # Treina o modelo
        # ----------------------------------------------------

        modelo = fit(X_treino, y_treino)

        # ----------------------------------------------------
        # Faz previsões
        # ----------------------------------------------------

        previsoes = predict(modelo, X_teste)

        # ----------------------------------------------------
        # Calcula o erro
        # ----------------------------------------------------

        erro = loss(y_teste, previsoes)

        erros.append(erro)

    # Média dos erros dos k folds
    return np.mean(erros)


# ============================================================
# 3. KNN
# ============================================================

def fit_knn(X, y, k):
    """
    'Treina' o kNN.

    Como kNN não possui uma etapa tradicional de treinamento,
    simplesmente guardamos os dados e o valor de k.
    """

    modelo = {
        "X": X,
        "y": y,
        "k": k
    }

    return modelo


def predict_knn(modelo, X):
    """
    Faz previsões usando kNN.
    """

    X_treino = modelo["X"]
    y_treino = modelo["y"]
    k = modelo["k"]

    previsoes = []

    for x in X:

        # ----------------------------------------------------
        # Calcula a distância de x para todos os pontos
        # de treinamento
        # ----------------------------------------------------

        distancias = np.linalg.norm(X_treino - x, axis=1)

        # ----------------------------------------------------
        # Pega os índices dos k vizinhos mais próximos
        # ----------------------------------------------------

        indices = np.argsort(distancias)[:k]

        # Classes dos vizinhos
        classes = y_treino[indices]

        # ----------------------------------------------------
        # Votação majoritária
        # ----------------------------------------------------

        valores, contagens = np.unique(
            classes,
            return_counts=True
        )

        classe_predita = valores[np.argmax(contagens)]

        previsoes.append(classe_predita)

    return np.array(previsoes)


# ============================================================
# 4. FUNÇÃO DE LOSS
# ============================================================

def erro_classificacao(y_real, y_pred):
    """
    Erro de classificação:

        número de classificações erradas / número total
    """

    return np.mean(y_real != y_pred)


# ============================================================
# 5. CRIA UMA FUNÇÃO fit PARA UM k ESPECÍFICO
# ============================================================

def make_fit_knn(k):
    """
    Cria uma função fit(X, y) que utiliza o k especificado.
    """

    def fit(X, y):
        return fit_knn(X, y, k)

    return fit


# ============================================================
# 6. DADOS SINTÉTICOS
# ============================================================

np.random.seed(42)

# Classe 0
X0 = np.random.randn(50, 2) + np.array([-2, -2])

# Classe 1
X1 = np.random.randn(50, 2) + np.array([2, 2])

# Junta os dados
X = np.vstack([X0, X1])

# Rótulos
y = np.array([0] * 50 + [1] * 50)


# ============================================================
# 7. TESTANDO DIFERENTES VALORES DE k
# ============================================================

valores_k = [1, 3, 5, 7, 9, 11, 15, 20]

print("=" * 55)
print("VALIDAÇÃO CRUZADA K-FOLD")
print("=" * 55)

erros_cv = []

for k in valores_k:

    erro = k_fold(
        X,
        y,
        5,                    # 5-fold
        make_fit_knn(k),      # fit
        predict_knn,          # predict
        erro_classificacao    # loss
    )

    erros_cv.append(erro)

    print(f"k = {k:2d} | erro CV = {erro:.3f}")


# ============================================================
# 8. MELHOR k SEGUNDO A VALIDAÇÃO CRUZADA
# ============================================================

indice_melhor_cv = np.argmin(erros_cv)

k_melhor_cv = valores_k[indice_melhor_cv]

erro_melhor_cv = erros_cv[indice_melhor_cv]


# ============================================================
# 9. ERRO DE TREINO
# ============================================================

erros_treino = []

print()
print("=" * 55)
print("ERRO DE TREINO")
print("=" * 55)

for k in valores_k:

    # Treina usando TODOS os dados
    modelo = fit_knn(X, y, k)

    # Prediz nos próprios dados de treinamento
    previsoes = predict_knn(modelo, X)

    # Calcula erro
    erro = erro_classificacao(y, previsoes)

    erros_treino.append(erro)

    print(f"k = {k:2d} | erro treino = {erro:.3f}")


# ============================================================
# 10. MELHOR k SEGUNDO O ERRO DE TREINO
# ============================================================

indice_melhor_treino = np.argmin(erros_treino)

k_melhor_treino = valores_k[indice_melhor_treino]

erro_melhor_treino = erros_treino[indice_melhor_treino]


# ============================================================
# 11. COMPARAÇÃO FINAL
# ============================================================

print()
print("=" * 55)
print("COMPARAÇÃO")
print("=" * 55)

print(
    f"Melhor k pelo erro de treino: "
    f"{k_melhor_treino}"
)

print(
    f"Erro de treino: "
    f"{erro_melhor_treino:.3f}"
)

print()

print(
    f"Melhor k pela validação cruzada: "
    f"{k_melhor_cv}"
)

print(
    f"Erro de validação cruzada: "
    f"{erro_melhor_cv:.3f}"
)