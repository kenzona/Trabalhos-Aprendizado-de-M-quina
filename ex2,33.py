
import numpy as np


# ============================================================
# 1. Função sigmoide e distribuição eta(x)
# ============================================================

def sigmoid(t):
    return 1 / (1 + np.exp(-t))


def eta(x):
    """
    eta(x) = P(Y=1 | X=x)
           = sigmoid(10 * (x1 - x2))

    x pode ser:
    - vetor de shape (2,)
    - matriz de shape (n, 2)
    """
    x = np.asarray(x)
    return sigmoid(10 * (x[..., 0] - x[..., 1]))


# ============================================================
# 2. Gerar dados
# ============================================================

def generate_data(n, rng):
    """
    Gera:
        X ~ Uniforme([0,1]^2)
        Y | X=x ~ Bernoulli(eta(x))
    """

    X = rng.random((n, 2))

    probabilities = eta(X)

    y = (rng.random(n) < probabilities).astype(int)

    return X, y


# ============================================================
# 3. Distância euclidiana
# ============================================================

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))


# ============================================================
# 4. Classificador kNN
# ============================================================

def knn_class(X, y, x0, k, distance=euclidean_distance):
    """
    Classificador kNN.

    Parâmetros:
        X        : dados de treinamento
        y        : rótulos
        x0       : ponto a classificar
        k        : número de vizinhos
        distance : função de distância

    Desempate:
        menor rótulo.
    """

    distances = []

    for i in range(len(X)):
        d = distance(X[i], x0)
        distances.append((d, y[i]))

    # Ordena pela distância
    distances.sort(key=lambda pair: pair[0])

    # Pega os k vizinhos mais próximos
    neighbors = distances[:k]

    # Conta os votos
    counts = {}

    for _, label in neighbors:
        counts[label] = counts.get(label, 0) + 1

    # Maior número de votos
    max_count = max(counts.values())

    # Classes empatadas
    tied_labels = []

    for label in counts:
        if counts[label] == max_count:
            tied_labels.append(label)

    # Desempate pelo menor rótulo
    return min(tied_labels)


# ============================================================
# 5. Classificador de Bayes
# ============================================================

def bayes(x0):
    """
    Como:
        P(Y=1 | X=x) = eta(x)

    então:
        P(Y=0 | X=x) = 1 - eta(x)

    Com perda 0-1, Bayes escolhe a classe mais provável.
    """

    p1 = eta(x0)

    if p1 >= 0.5:
        return 1
    else:
        return 0


# ============================================================
# 6. Prever vários pontos
# ============================================================

def predict_knn(X_train, y_train, X_test, k,
                distance=euclidean_distance):

    predictions = []

    for x in X_test:
        prediction = knn_class(
            X_train,
            y_train,
            x,
            k,
            distance
        )
        predictions.append(prediction)

    return np.array(predictions)


def predict_bayes(X_test):

    predictions = []

    for x in X_test:
        predictions.append(bayes(x))

    return np.array(predictions)


# ============================================================
# 7. Taxa de erro
# ============================================================

def error_rate(y_true, y_pred):
    return np.mean(y_true != y_pred)


# ============================================================
# 8. Validação cruzada
# ============================================================

def choose_k_cv(X, y, k_values, folds=5, rng=None):
    """
    Escolhe o melhor k usando validação cruzada.

    Critério:
        menor erro médio.

    Em caso de empate:
        escolhe o menor k.
    """

    if rng is None:
        rng = np.random.default_rng()

    n = len(X)

    # Embaralha os índices
    indices = rng.permutation(n)

    # Divide em folds
    folds_indices = np.array_split(indices, folds)

    best_k = None
    best_error = float("inf")

    for k in k_values:

        fold_errors = []

        for i in range(folds):

            # Fold atual = validação
            val_idx = folds_indices[i]

            # Restante = treinamento
            train_idx = np.concatenate([
                folds_indices[j]
                for j in range(folds)
                if j != i
            ])

            X_train = X[train_idx]
            y_train = y[train_idx]

            X_val = X[val_idx]
            y_val = y[val_idx]

            # k não pode ser maior que o treino
            k_actual = min(k, len(X_train))

            y_pred = predict_knn(
                X_train,
                y_train,
                X_val,
                k_actual
            )

            fold_errors.append(
                error_rate(y_val, y_pred)
            )

        mean_error = np.mean(fold_errors)

        # Se encontrou erro menor
        # ou empate com k menor
        if (mean_error < best_error or
            (mean_error == best_error and
             (best_k is None or k < best_k))):

            best_error = mean_error
            best_k = k

    return best_k, best_error


# ============================================================
# 9. Experimento principal
# ============================================================

rng = np.random.default_rng(42)

N_values = [50, 200, 1000, 5000]

# Conjunto de teste grande
N_test = 10000

X_test, y_test = generate_data(N_test, rng)

# Valores candidatos para k
k_values = [
    1, 3, 5, 7, 9,
    15, 25, 35, 51
]

results = []


for N in N_values:

    print("=" * 60)
    print(f"N = {N}")

    # --------------------------------------------------------
    # Gera treinamento
    # --------------------------------------------------------

    X_train, y_train = generate_data(N, rng)

    # --------------------------------------------------------
    # Escolhe k por validação cruzada
    # --------------------------------------------------------

    possible_k = [
        k for k in k_values
        if k <= N * 0.8
    ]

    best_k, cv_error = choose_k_cv(
        X_train,
        y_train,
        possible_k,
        folds=5,
        rng=rng
    )

    # --------------------------------------------------------
    # kNN no conjunto de teste
    # --------------------------------------------------------

    y_pred_knn = predict_knn(
        X_train,
        y_train,
        X_test,
        best_k
    )

    knn_error = error_rate(
        y_test,
        y_pred_knn
    )

    # --------------------------------------------------------
    # Bayes no conjunto de teste
    # --------------------------------------------------------

    y_pred_bayes = predict_bayes(X_test)

    bayes_error = error_rate(
        y_test,
        y_pred_bayes
    )

    # --------------------------------------------------------
    # Diferença
    # --------------------------------------------------------

    difference = knn_error - bayes_error

    results.append({
        "N": N,
        "best_k": best_k,
        "cv_error": cv_error,
        "knn_error": knn_error,
        "bayes_error": bayes_error,
        "difference": difference
    })

    print(f"Melhor k:       {best_k}")
    print(f"Erro CV:        {cv_error:.4f}")
    print(f"Erro kNN:       {knn_error:.4f}")
    print(f"Erro Bayes:     {bayes_error:.4f}")
    print(f"Diferença:      {difference:.4f}")


# ============================================================
# 10. Mostrar resultados finais
# ============================================================

print("\n")
print("=" * 75)
print("RESULTADOS FINAIS")
print("=" * 75)

print(
    f"{'N':>6}"
    f"{'k':>6}"
    f"{'Erro kNN':>14}"
    f"{'Erro Bayes':>14}"
    f"{'Diferença':>14}"
)

for result in results:

    print(
        f"{result['N']:>6}"
        f"{result['best_k']:>6}"
        f"{result['knn_error']:>14.4f}"
        f"{result['bayes_error']:>14.4f}"
        f"{result['difference']:>14.4f}"
    )