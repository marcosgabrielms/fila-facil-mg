# Lab 01 — Validador de senha

Primeiro laboratório da disciplina. Cobre as Unidades 3 (contexto e especificação) e
4 (fluxo de desenvolvimento verificável).

## O problema

Implementar uma função que avalia se uma senha atende a uma política de segurança e
que, ao rejeitar, informa **todos** os motivos — não apenas o primeiro.

## O que fazer

1. Leia [`ESPECIFICACAO.md`](ESPECIFICACAO.md) inteiro. É o documento normativo.
2. Implemente `validar_senha` em `src/validador_senha/validador.py`.
3. Rode os testes até tudo passar.
4. Registre o processo em [`prompts/`](prompts/) e [`evidencias/`](evidencias/).

```bash
uv run pytest labs/lab-01-validador-senha
```

São 53 testes. Todos começam vermelhos.

## Um aviso sobre este laboratório

A política de senha é simples de entender. A dificuldade está nas **definições** da
seção 4 da especificação — e ela foi escrita assim de propósito.

Qualquer ferramenta de IA produz uma solução plausível para este problema em segundos.
A maioria dessas soluções **falha nos testes**, porque usa `str.isupper()`,
`str.isdigit()` e afins, que seguem regras Unicode, enquanto a especificação exige ASCII
estrito.

Esse é o ponto do exercício. Não é uma pegadinha contra você: é a demonstração de por
que especificação precisa ser precisa e por que teste é o que separa código plausível de
código correto.

## Não altere os testes

`tests/` é o árbitro comum do experimento comparativo. Se você acredita que algum teste
contradiz a especificação, abra uma issue descrevendo a contradição. Isso conta a favor.
