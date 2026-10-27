Abaixo está um README completo, pronto para colocar no projeto como `README.md`.

# Exercício 2.4 — Interpolação de Lagrange e sua instabilidade

## Objetivo

Este exercício implementa o polinômio interpolador de Lagrange e analisa sua estabilidade quando os valores observados possuem ruído.

O objetivo é observar que, embora o polinômio interpolador passe exatamente por todos os dados de treinamento, pequenas mudanças no ruído podem produzir valores diferentes para o polinômio estimado.

O modelo considerado é:

$$
Y=f(X)+\varepsilon
$$

onde:

* \(f(X)\) representa a função verdadeira;
* \(\varepsilon\) representa o ruído;
* \(Y\) representa os valores observados.

Neste exercício:

$$
f(x)=\sin(3x)
$$

e:

$$
\varepsilon_i\sim N(0,0.1^2).
$$

---

## Implementação da interpolação de Lagrange

O polinômio interpolador de Lagrange é definido por:

$$
p(x)=\sum_{i=1}^{N}y_iL_i(x)
$$

onde cada polinômio básico \(L_i(x)\) é:

$$
L_i(x)=
\prod_{j\neq i}
\frac{x-x_j}{x_i-x_j}.
$$

A principal propriedade desses polinômios é:

$$
L_i(x_k)=
\begin{cases}
1, & i=k\\
0, & i\neq k
\end{cases}
$$

Portanto:

$$
p(x_k)
=
\sum_{i=1}^{N}y_iL_i(x_k)
=
y_k.
$$

Isso garante que o polinômio interpolador passa exatamente por todos os pontos fornecidos.

---

## Função `lagrange`

```python
def lagrange(xs, ys):

    n = len(xs)

    def p(x):
        resultado = 0.0

        for i in range(n):

            Li = 1.0

            for j in range(n):
                if i != j:
                    Li *= (
                        (x - xs[j])
                        /
                        (xs[i] - xs[j])
                    )

            resultado += ys[i] * Li

        return resultado

    return p
```

A função recebe:

* `xs`: valores \(x_1,\ldots,x_N\);
* `ys`: valores \(y_1,\ldots,y_N\).

Ela retorna uma nova função:

```python
p(x)
```

que calcula o valor do polinômio interpolador em qualquer ponto \(x\).

---

## Como o código funciona

Primeiramente, para cada ponto \(i\), calculamos o polinômio básico:

```python
Li = 1.0

for j in range(n):
    if i != j:
        Li *= (x - xs[j]) / (xs[i] - xs[j])
```

Esse trecho implementa:

$$
L_i(x)=
\prod_{j\neq i}
\frac{x-x_j}{x_i-x_j}.
$$

Depois multiplicamos esse polinômio pelo valor correspondente \(y_i\):

```python
resultado += ys[i] * Li
```

Isso implementa:

$$
p(x)=\sum_i y_iL_i(x).
$$

Ao final, a função retorna o valor:

$$
p(x).
$$

---

# Experimento

## Pontos utilizados

Foram utilizados 10 pontos igualmente espaçados no intervalo:

$$
[-1,1].
$$

No código:

```python
xs = np.linspace(-1, 1, 10)
```

Isso gera:

$$
x_1,\ldots,x_{10}.
$$

---

## Função verdadeira

A função escolhida pelo exercício é:

$$
f(x)=\sin(3x).
$$

No código:

```python
def f(x):
    return np.sin(3 * x)
```

---

## Adicionando ruído

Os valores observados são gerados por:

$$
y_i=f(x_i)+\varepsilon_i
$$

onde:

$$
\varepsilon_i\sim N(0,0.1^2).
$$

No código:

```python
eps = np.random.normal(
    loc=0,
    scale=0.1,
    size=10
)

ys = f(xs) + eps
```

O parâmetro:

```python
loc=0
```

representa a média:

$$
E[\varepsilon]=0.
$$

O parâmetro:

```python
scale=0.1
```

representa o desvio padrão:

$$
\sigma=0.1.
$$

Portanto, a variância é:

$$
\sigma^2=0.01=0.1^2.
$$

---

# Avaliação do interpolador

O ponto escolhido é:

$$
x_0=0.95.
$$

No código:

```python
x0 = 0.95
```

Depois de construir o interpolador:

```python
p = lagrange(xs, ys)
```

avaliamos:

```python
p(x0)
```

e comparamos com o valor verdadeiro:

```python
f(x0)
```

Matematicamente, comparamos:

$$
p(0.95)
$$

com:

$$
f(0.95)=\sin(3\cdot0.95).
$$

Ou seja:

$$
f(0.95)=\sin(2.85).
$$

Aproximadamente:

$$
\boxed{
f(0.95)\approx0.2875
}
$$

---

# Repetindo o experimento

O experimento é repetido 100 vezes:

```python
valores = []

for _ in range(100):

    eps = np.random.normal(
        loc=0,
        scale=0.1,
        size=10
    )

    ys = f(xs) + eps

    p = lagrange(xs, ys)

    valores.append(p(x0))
```

Em cada repetição:

1. Os valores \(x_i\) permanecem iguais;
2. A função verdadeira \(f\) permanece igual;
3. Apenas o ruído \(\varepsilon_i\) é reamostrado;
4. Um novo conjunto de valores \(y_i\) é criado;
5. Um novo polinômio interpolador é construído;
6. O valor \(p(0.95)\) é armazenado.

Assim, obtemos:

$$
p_1(0.95),
p_2(0.95),
\ldots,
p_{100}(0.95).
$$

---

# Média e desvio padrão

Após realizar as 100 repetições, calculamos:

```python
media = np.mean(valores)
```

que corresponde a:

$$
\frac{1}{100}
\sum_{k=1}^{100}p_k(x_0).
$$

Também calculamos o desvio padrão:

```python
desvio_padrao = np.std(
    valores,
    ddof=1
)
```

O desvio padrão mede o quanto os valores:

$$
p_1(x_0),
p_2(x_0),
\ldots,
p_{100}(x_0)
$$

variam quando apenas o ruído é modificado.

---

# Resultados

Os valores exatos dependem do ruído gerado aleatoriamente. Portanto, cada execução pode produzir resultados diferentes.

O programa reporta:

```text
Média de p(x0): ...
Desvio padrão de p(x0): ...
f(x0): 0.2875...
```

A comparação principal é entre:

$$
\text{Média de }p(0.95)
$$

e:

$$
f(0.95).
$$

---

# Por que o interpolador é instável?

O polinômio interpolador pode ser escrito como:

$$
p(x_0)
=
\sum_{i=1}^{10}y_iL_i(x_0).
$$

Como:

$$
y_i=f(x_i)+\varepsilon_i,
$$

temos:

$$
p(x_0)
=
\sum_i
\left[f(x_i)+\varepsilon_i\right]
L_i(x_0).
$$

Separando os termos:

$$
p(x_0)
=
\sum_i f(x_i)L_i(x_0)
+
\sum_i\varepsilon_iL_i(x_0).
$$

O primeiro termo representa a parte relacionada à função verdadeira:

$$
\sum_i f(x_i)L_i(x_0).
$$

O segundo termo representa a influência do ruído:

$$
\boxed{
\sum_i\varepsilon_iL_i(x_0)
}
$$

Portanto, mesmo pequenas mudanças em:

$$
\varepsilon_i
$$

podem alterar o valor final:

$$
p(x_0).
$$

Isso ocorre porque os polinômios \(L_i(x_0)\) podem amplificar o ruído.

---

# Relação com a variância

Supondo que os ruídos sejam independentes e tenham:

$$
\operatorname{Var}(\varepsilon_i)=\sigma^2,
$$

podemos escrever:

$$
p(x_0)
=
\text{parte determinística}
+
\sum_iL_i(x_0)\varepsilon_i.
$$

Então:

$$
\boxed{
\operatorname{Var}(p(x_0))
=
\sigma^2
\sum_iL_i(x_0)^2
}
$$

No exercício:

$$
\sigma=0.1.
$$

Portanto:

$$
\operatorname{Var}(p(x_0))
=
0.01
\sum_iL_i(x_0)^2.
$$

Se os valores dos polinômios básicos forem grandes, o ruído será amplificado e o valor de:

$$
p(x_0)
$$

terá uma variância maior.

---

# Conclusão

O experimento mostra que o polinômio interpolador possui erro empírico zero:

$$
p(x_i)=y_i
$$

para todos os pontos observados.

Porém, isso não significa que ele tenha aprendido perfeitamente a função verdadeira:

$$
f(x)=\sin(3x).
$$

Os valores observados são:

$$
y_i=f(x_i)+\varepsilon_i,
$$

portanto o interpolador ajusta não apenas a função \(f\), mas também o ruído:

$$
\boxed{
\text{dados observados}
=
\text{função verdadeira}
+
\text{ruído}
}
$$

Ao repetir o experimento mantendo os mesmos \(x_i\) e alterando apenas o ruído, obtemos diferentes polinômios interpoladores e diferentes valores para:

$$
p(0.95).
$$

Assim, o experimento evidencia que o interpolador pode ser sensível a pequenas mudanças nos dados. Essa sensibilidade será posteriormente descrita pelo conceito de:

$$
\boxed{\text{variância}}
$$

Um método com alta variância produz estimativas muito diferentes quando o conjunto de dados muda ligeiramente, mesmo que o processo gerador dos dados continue sendo o mesmo.

A principal conclusão é:

$$
\boxed{
\text{Interpolar perfeitamente os dados não significa necessariamente aprender bem }f.
}
$$
