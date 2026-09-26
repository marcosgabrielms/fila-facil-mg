# AGENTS.md — Laboratório 01, validador de senha

Instruções específicas deste laboratório. Valem **junto com** o `AGENTS.md` da raiz do
repositório; em caso de conflito, este prevalece por ser mais específico.

## O problema

Implementar `validar_senha` em `src/validador_senha/validador.py`, conforme
`ESPECIFICACAO.md`.

## Antes de escrever qualquer código

Leia `ESPECIFICACAO.md` **inteiro**, com atenção especial à seção 4.

A seção 4 define maiúscula, minúscula, dígito, caractere especial e espaço em branco.
Essas definições **não** coincidem com o comportamento padrão dos métodos de `str` do
Python, e a divergência é deliberada:

- `str.isupper()`, `str.islower()`, `str.isdigit()` e `str.isalpha()` seguem regras
  Unicode. A especificação exige ASCII estrito para maiúscula, minúscula e dígito.
  Usar esses métodos diretamente **viola a especificação** e falha nos testes.
- Espaço em branco, ao contrário, usa a regra Unicode de `str.isspace()`. A
  inconsistência entre as duas coisas é intencional e está justificada no texto.

Uma solução escrita no automático usa os métodos de `str` e quebra em `"Ç"`, `"é"`,
`"٣"` e `"Ⅳ"`. Se você é um agente e está prestes a fazer isso, releia a seção 4.

## Contrato imutável

A dataclass `ResultadoValidacao` e a assinatura de `validar_senha` fazem parte da
especificação. Não altere nenhuma das duas.

## Escopo fechado

Fora deste laboratório, conforme a seção 7 da especificação: entropia, verificação de
vazamentos, hashing, internacionalização e interface. Resolve-se com a biblioteca
padrão — nenhuma dependência nova.

## Como saber que terminou

```bash
uv run pytest labs/lab-01-validador-senha
```

53 testes, todos verdes. Cada teste corresponde a um critério de aceitação da seção 6.
