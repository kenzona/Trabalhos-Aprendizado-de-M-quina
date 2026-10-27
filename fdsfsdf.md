## (c) Colocando o problema na forma padrão

O modelo obtido no item anterior é:

$$
\begin{aligned}
\max \quad & z=1000x_{\text{prod}}+2100x_{\text{inst}}+16000\\
\text{sujeito a}\quad
&x_{\text{prod}}+x_{\text{inst}}=40,\\
&x_{\text{prod}}+3x_{\text{inst}}\geq30,\\
&x_{\text{prod}},x_{\text{inst}}\geq0.
\end{aligned}
$$

Para aplicar o Método Simplex, devemos transformar as restrições em igualdades.

### Restrição de alocação dos trabalhadores

A primeira restrição já está na forma de igualdade:

$$
x_{\text{prod}}+x_{\text{inst}}=40.
$$

Como uma restrição de igualdade não possui naturalmente uma variável de folga que possa entrar na base inicial, introduzimos uma variável artificial \(a_1\):

$$
\boxed{x_{\text{prod}}+x_{\text{inst}}+a_1=40}.
$$

---

### Restrição de produção mínima

A segunda restrição é:

$$
x_{\text{prod}}+3x_{\text{inst}}\geq30.
$$

Como se trata de uma desigualdade do tipo \(\geq\), introduzimos uma variável de excesso \(s\geq0\), subtraindo-a do lado esquerdo:

$$
x_{\text{prod}}+3x_{\text{inst}}-s=30.
$$

Entretanto, a variável de excesso possui coeficiente \(-1\), portanto ela não fornece uma variável básica inicial. Assim, introduzimos uma variável artificial \(a_2\):

$$
\boxed{x_{\text{prod}}+3x_{\text{inst}}-s+a_2=30}.
$$

---

### Forma padrão

Assim, o problema na forma padrão para aplicação do Método Simplex é:

$$
\boxed{
\begin{aligned}
\max\quad
&z=1000x_{\text{prod}}+2100x_{\text{inst}}+16000\\
\text{sujeito a}\quad
&x_{\text{prod}}+x_{\text{inst}}+a_1=40,\\
&x_{\text{prod}}+3x_{\text{inst}}-s+a_2=30,\\
&x_{\text{prod}},x_{\text{inst}},s,a_1,a_2\geq0.
\end{aligned}
}
$$

onde:

$$
\begin{aligned}
x_{\text{prod}}&=\text{número de trabalhadores destinados à produção},\\
x_{\text{inst}}&=\text{número de trabalhadores destinados ao treinamento},\\
s&=\text{variável de excesso da restrição de produção},\\
a_1,a_2&=\text{variáveis artificiais}.
\end{aligned}
$$

As variáveis artificiais \(a_1\) e \(a_2\) são utilizadas apenas para obter uma base inicial viável. Portanto, para resolver o problema utilizando o tableau tradicional, seria necessário aplicar o Método Simplex de Duas Fases ou o Método do Big M.

No entanto, como a igualdade

$$
x_{\text{prod}}+x_{\text{inst}}=40
$$

permite escrever diretamente:

$$
\boxed{x_{\text{prod}}=40-x_{\text{inst}}},
$$

podemos resolver o problema de maneira mais simples utilizando o Método Simplex na forma de dicionário, como será feito no item (d).
