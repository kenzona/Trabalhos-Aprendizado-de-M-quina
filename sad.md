## (d) Resolução pelo Método Simplex — Forma de Dicionário

Vamos resolver o problema utilizando o **Método Simplex na forma de dicionário**. Essa abordagem é particularmente adequada neste problema, pois a restrição de igualdade permite escrever diretamente uma variável básica em função da variável não básica.

### 1. Solução básica inicial

A restrição de alocação dos trabalhadores é:

$$
x_{\text{prod}}+x_{\text{inst}}=40.
$$

Inicialmente, escolhemos \(x_{\text{prod}}\) como variável básica e \(x_{\text{inst}}\) como variável não básica. Assim, o dicionário inicial é:

$$
\boxed{x_{\text{prod}}=40-x_{\text{inst}}}.
$$

Fazendo a variável não básica igual a zero,

$$
x_{\text{inst}}=0,
$$

obtemos a solução básica:

$$
x_{\text{prod}}=40.
$$

Portanto, a solução básica inicial é:

$$
\boxed{(x_{\text{prod}},x_{\text{inst}})=(40,0)}.
$$

---

### 2. Verificação da restrição de produção

A restrição de produção mínima é:

$$
x_{\text{prod}}+3x_{\text{inst}}\geq30.
$$

Substituindo o dicionário:

$$
(40-x_{\text{inst}})+3x_{\text{inst}}\geq30.
$$

Logo:

$$
40+2x_{\text{inst}}\geq30,
$$

ou equivalentemente:

$$
x_{\text{inst}}\geq-5.
$$

Como já temos a condição de não negatividade:

$$
x_{\text{inst}}\geq0,
$$

concluímos que a restrição de produção é automaticamente satisfeita para toda solução viável. Portanto, ela não limita o movimento do Simplex e é redundante.

---

### 3. Dicionário da função objetivo

A função objetivo é:

$$
z=1000x_{\text{prod}}+2100x_{\text{inst}}+16000.
$$

Substituindo:

$$
x_{\text{prod}}=40-x_{\text{inst}},
$$

temos:

$$
z=1000(40-x_{\text{inst}})
+2100x_{\text{inst}}
+16000.
$$

Simplificando:

$$
\boxed{z=56000+1100x_{\text{inst}}}.
$$

O coeficiente da variável não básica \(x_{\text{inst}}\) é o seu **custo reduzido**:

$$
\boxed{\bar c_{\text{inst}}=1100}.
$$

Como:

$$
\bar c_{\text{inst}}>0,
$$

aumentar \(x_{\text{inst}}\) aumenta o valor da função objetivo. Assim, de acordo com o Método Simplex para um problema de maximização:

$$
\boxed{x_{\text{inst}}\text{ entra na base}}.
$$

---

### 4. Teste da razão e variável que sai da base

Para manter a viabilidade da solução, devemos preservar:

$$
x_{\text{prod}}\geq0.
$$

Utilizando o dicionário:

$$
x_{\text{prod}}=40-x_{\text{inst}},
$$

temos:

$$
40-x_{\text{inst}}\geq0.
$$

Portanto:

$$
\boxed{x_{\text{inst}}\leq40}.
$$

Assim, podemos aumentar \(x_{\text{inst}}\) até:

$$
x_{\text{inst}}=40.
$$

Nesse ponto:

$$
x_{\text{prod}}=40-40=0.
$$

Logo, o teste da razão determina que:

$$
\boxed{x_{\text{prod}}\text{ sai da base}}.
$$

O novo ponto básico é:

$$
\boxed{(x_{\text{prod}},x_{\text{inst}})=(0,40)}.
$$

---

### 5. Novo dicionário

Após o pivotamento, \(x_{\text{inst}}\) passa a ser a variável básica. Da igualdade:

$$
x_{\text{prod}}+x_{\text{inst}}=40,
$$

obtemos:

$$
\boxed{x_{\text{inst}}=40-x_{\text{prod}}}.
$$

Substituindo na função objetivo:

$$
z=56000+1100(40-x_{\text{prod}}).
$$

Portanto:

$$
\boxed{z=100000-1100x_{\text{prod}}}.
$$

Agora, \(x_{\text{prod}}\) é a variável não básica e possui custo reduzido:

$$
\boxed{\bar c_{\text{prod}}=-1100<0}.
$$

Como aumentar \(x_{\text{prod}}\) diminuiria o valor da função objetivo, não existe nenhuma variável não básica capaz de melhorar \(z\).

Portanto, pelo critério de otimalidade do Método Simplex, a solução atual é ótima.

---

### 6. Solução ótima

A solução ótima é:

$$
\boxed{x_{\text{inst}}^*=40}
$$

e:

$$
\boxed{x_{\text{prod}}^*=0}.
$$

Portanto, todos os 40 trabalhadores experientes devem ser destinados ao treinamento na primeira semana.

Cada instrutor treina 3 novos trabalhadores, resultando em:

$$
3\cdot40=120
$$

novos trabalhadores disponíveis na segunda semana.

O lucro máximo é:

$$
z^*=56000+1100(40),
$$

logo:

$$
\boxed{z^*=\text{R\$ }100.000}.
$$

Portanto, a solução ótima do problema é:

$$
\boxed{
x_{\text{prod}}^*=0,\qquad
x_{\text{inst}}^*=40,\qquad
z^*=\text{R\$ }100.000
}.
$$
