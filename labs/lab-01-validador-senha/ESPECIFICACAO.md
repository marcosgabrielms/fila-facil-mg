# Especificação — Validador de Senha

> Documento normativo. Em caso de divergência entre esta especificação e qualquer outra
> fonte (código existente, sugestão de IA, intuição), **esta especificação prevalece**.

## 1. Problema

Precisamos de uma função que avalie se uma senha atende à política de segurança
definida abaixo e que, quando a senha for rejeitada, informe **todos** os motivos da
rejeição — não apenas o primeiro encontrado.

O consumidor dessa função é uma tela de cadastro que exibe a lista completa de
problemas para a pessoa usuária de uma só vez, evitando o vaivém de corrigir um erro
por tentativa.

## 2. Contrato

```python
def validar_senha(senha: str) -> ResultadoValidacao: ...
```

O tipo de retorno é:

```python
@dataclass(frozen=True)
class ResultadoValidacao:
    valida: bool
    erros: tuple[str, ...]
```

Regras do contrato:

- `valida` é `True` se e somente se `erros` estiver vazio.
- `erros` contém os **códigos** dos requisitos violados (por exemplo `"RF-01"`), nunca
  mensagens em texto livre.
- `erros` é ordenado de forma crescente pelo número do requisito. A ordem é
  determinística: a mesma senha sempre produz exatamente a mesma tupla.
- Nenhum código aparece repetido.

## 3. Requisitos funcionais

Cada requisito tem um código. O código é o que aparece em `erros` quando o requisito é
violado.

| Código | Requisito |
|---|---|
| RF-01 | A senha tem **no mínimo 8** caracteres. |
| RF-02 | A senha tem **no máximo 64** caracteres. |
| RF-03 | A senha contém pelo menos uma letra **maiúscula de A a Z**. |
| RF-04 | A senha contém pelo menos uma letra **minúscula de a a z**. |
| RF-05 | A senha contém pelo menos um **dígito de 0 a 9**. |
| RF-06 | A senha contém pelo menos um **caractere especial** (ver seção 4). |
| RF-07 | A senha **não contém** nenhum caractere de espaço em branco (ver seção 4). |
| RF-08 | A senha **não consta** na lista de senhas proibidas (ver seção 4). |

## 4. Definições precisas

Estas definições existem porque cada uma delas é uma armadilha conhecida. Leia com
atenção antes de implementar — e desconfie de qualquer solução que as ignore.

### 4.1 Maiúscula, minúscula e dígito são **restritos a ASCII**

- Maiúscula: exatamente os caracteres `A`–`Z`.
- Minúscula: exatamente os caracteres `a`–`z`.
- Dígito: exatamente os caracteres `0`–`9`.

Consequências obrigatórias:

- `"Ç"` **não** satisfaz RF-03. É maiúscula em português, mas não está no intervalo `A`–`Z`.
- `"é"` **não** satisfaz RF-04.
- `"٣"` (dígito arábico-índico) **não** satisfaz RF-05, embora `str.isdigit()` retorne
  `True` para ele em Python.
- `"Ⅳ"` (numeral romano Unicode) **não** satisfaz RF-05.

> Métodos como `str.isupper()`, `str.islower()`, `str.isdigit()` e `str.isalpha()`
> seguem regras Unicode e **não** implementam estas definições. Usá-los diretamente
> viola a especificação.

### 4.2 Caractere especial

Caractere especial é qualquer caractere pertencente ao seguinte conjunto, e nenhum
outro:

```
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

Este é exatamente o conjunto `string.punctuation` do Python. Um caractere fora desse
conjunto — por exemplo `"ç"`, `"é"`, `"€"` ou `"\t"` — **não** satisfaz RF-06.

### 4.3 Espaço em branco

Espaço em branco é qualquer caractere para o qual `str.isspace()` retorne `True`.
Isso inclui, entre outros, o espaço comum, a tabulação `\t`, a quebra de linha `\n`
e o espaço inquebrável ` `.

Aqui a regra Unicode **é** a desejada — diferentemente da seção 4.1. A diferença é
intencional: espaço em branco deve ser rejeitado em todas as suas formas.

### 4.4 Lista de senhas proibidas

A lista é exatamente esta, e faz parte da especificação:

```
123456
password
qwerty
senha123
admin
```

A comparação é **insensível a maiúsculas e minúsculas**: `"PASSWORD"`, `"Password"` e
`"password"` são todos rejeitados por RF-08.

A comparação é de **igualdade da senha inteira**, não de substring. `"password1"`
não viola RF-08 — a senha precisa ser exatamente igual a um item da lista, ignorando a
caixa.

## 5. Casos de borda obrigatórios

| Entrada | Comportamento esperado |
|---|---|
| `""` (string vazia) | Não é erro de programa. Retorna `valida=False` com os códigos de todos os requisitos violados. |
| Senha com 8 caracteres | Satisfaz RF-01. O limite é inclusivo. |
| Senha com 64 caracteres | Satisfaz RF-02. O limite é inclusivo. |
| Senha com 7 ou 65 caracteres | Viola RF-01 ou RF-02, respectivamente. |
| Argumento que não é `str` | Levanta `TypeError`. Não retorna `ResultadoValidacao`. |
| `None` | Levanta `TypeError`, pelo caso acima. |

A senha **não** deve sofrer nenhum tratamento prévio: nada de `strip()`, de
normalização Unicode ou de conversão de caixa antes da validação. A senha é avaliada
exatamente como recebida. A única exceção é a comparação de RF-08, que ignora a caixa
conforme a seção 4.4.

## 6. Critérios de aceitação

A implementação é aceita quando todos os critérios abaixo forem verdadeiros. Cada
critério tem um teste correspondente em `tests/test_validador_senha.py`.

| Critério | Descrição | Teste |
|---|---|---|
| CA-01 | Uma senha que atende a todos os requisitos retorna `valida=True` e `erros` vazio. | `test_ca01_senha_valida` |
| CA-02 | Cada requisito de RF-01 a RF-07, isoladamente violado, produz exatamente o seu código em `erros`. RF-08 não entra aqui: toda senha proibida já viola outros requisitos, então não existe violação isolada de RF-08. | `test_ca02_cada_requisito_isolado` |
| CA-03 | Uma senha que viola vários requisitos retorna **todos** os códigos correspondentes. | `test_ca03_multiplos_erros` |
| CA-04 | `erros` está sempre em ordem crescente de código e sem repetições. | `test_ca04_erros_ordenados_sem_repeticao` |
| CA-05 | Caracteres não-ASCII não satisfazem RF-03, RF-04 nem RF-05. | `test_ca05_nao_ascii_nao_conta` |
| CA-06 | Os limites de 8 e 64 caracteres são inclusivos. | `test_ca06_limites_inclusivos` |
| CA-07 | Todas as formas de espaço em branco violam RF-07. | `test_ca07_espacos_em_branco` |
| CA-08 | A lista de senhas proibidas é comparada ignorando a caixa e por igualdade total. | `test_ca08_senhas_proibidas` |
| CA-09 | Entrada que não é `str` levanta `TypeError`. | `test_ca09_tipo_invalido` |
| CA-10 | `valida` é `True` se e somente se `erros` estiver vazio, para qualquer entrada. | `test_ca10_coerencia_valida_erros` |

## 7. Fora de escopo

Não faz parte deste exercício: medir força de senha por entropia, verificar vazamentos
em bases externas, aplicar hashing, internacionalizar mensagens ou construir interface.
Propostas que ampliem o escopo serão consideradas desvio da especificação.
