# AGENTS.md — regras gerais do repositório

Instruções persistentes para agentes de programação, válidas em **todo** este
repositório.

Este arquivo segue o formato aberto de <https://agents.md/>. É lido por Codex, Claude
Code, OpenCode, Antigravity e outras ferramentas — a mesma instrução vale para todas.
A neutralidade é intencional e faz parte do conteúdo da disciplina: o contexto pertence
ao repositório, não à ferramenta.

## Instruções em camadas

Cada laboratório tem o **seu próprio** `AGENTS.md`, com as regras específicas dele.

```
AGENTS.md                                  ← este arquivo, vale em tudo
labs/lab-01-validador-senha/AGENTS.md      ← vale dentro deste laboratório
```

Quando você trabalha em um laboratório, valem os dois: este e o de lá. O mais
específico prevalece em caso de conflito.

Essa hierarquia é conteúdo da Unidade 3, não detalhe de organização. Vale abrir os dois
arquivos e observar o agente respeitando os dois níveis.

## O que é este repositório

Repositório-base da disciplina TEC.1053 — Tópicos Especiais em Programação (IFPI,
Tecnologia em ADS, 2026/2). Reúne os laboratórios do semestre. Cada laboratório é um
problema pequeno e fechado, resolvido por toda a turma com a mesma especificação e os
mesmos testes, variando modelo e ferramenta.

O projeto final de cada equipe **não** fica aqui — vai para repositório próprio.

## Estrutura

```
docs/         guias da disciplina: instalação, trilhas de IA, como registrar
labs/         um diretório por laboratório, autocontido
templates/    fichas em branco e modelo de relatório comparativo
```

## Comandos

```bash
uv run pytest                              # todos os laboratórios
uv run pytest labs/lab-01-validador-senha  # apenas um
uv run ruff check .                        # análise estática
uv run ruff format .                       # formatação
```

Não é preciso criar ambiente virtual nem instalar Python: o `uv` resolve a partir de
`.python-version` e `uv.lock`.

## Regras válidas em todo o repositório

**Não altere os testes.** Eles são o árbitro comum: soluções de modelos diferentes são
julgadas pela mesma régua. Uma solução que passa porque o teste foi afrouxado não
resolveu o problema. Se você acredita que um teste contradiz a especificação, relate a
contradição em vez de editar o teste.

**A especificação do laboratório é normativa.** Em qualquer divergência entre a
especificação, o código existente e o que parecer razoável, a especificação vence.

**Não amplie o escopo.** Cada especificação tem uma seção do que está fora. Não
adicione dependências sem necessidade demonstrada — os laboratórios são resolvíveis com
a biblioteca padrão.

**Não invente requisitos.** Se a especificação é omissa sobre um caso, diga que é
omissa. Não preencha a lacuna silenciosamente com uma suposição.

**Faça incrementos pequenos**, com os testes rodando entre eles.

**Trabalhe dentro de um laboratório por vez.** Não altere arquivos de outro laboratório
para resolver o que está em aberto no atual.

## Registro do trabalho

A disciplina avalia processo, não só resultado. Cada laboratório tem `prompts/` e
`evidencias/`. Ao concluir uma tarefa relevante, registre nos dois. As fichas em branco
estão em `templates/`, e o guia está em `docs/como-registrar.md`.

## Convenções de código

- Python 3.13, tipagem nas assinaturas públicas.
- Docstrings no formato Google, em português.
- Identificadores em português, acompanhando o domínio do problema.
- `ruff` com as regras de `pyproject.toml` decide estilo. Não discuta formatação.

## Segurança

Nunca escreva credenciais, tokens ou chaves de API no repositório, nem em `prompts/`
ou `evidencias/`. Ao colar saída de terminal, remova qualquer segredo antes.
