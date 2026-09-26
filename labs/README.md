# Laboratórios

Cada laboratório é um problema pequeno e fechado, com especificação normativa,
critérios de aceitação e suíte de testes. Toda a turma resolve o mesmo problema com a
mesma régua — o que varia é o modelo, a ferramenta e o caminho.

| Lab | Tema | Unidade | Situação |
|---|---|---|---|
| [01](lab-01-validador-senha/) | Validador de senha | 3 e 4 | Disponível |
| [02](lab-02-fila-facil/) | Fila Fácil — aplicação e supervisão de agente | 2, com apoio de 3 e 4 | Disponível |

Os demais serão publicados ao longo do semestre. Antes de atualizar um fork, confira
`git status --short` e preserve alterações locais. O tutorial do Lab 02 explica a atualização segura.

## Anatomia de um laboratório

```
lab-NN-nome/
├── ESPECIFICACAO.md   documento normativo: requisitos e critérios de aceitação
├── AGENTS.md          instruções específicas para agentes neste laboratório
├── src/               onde você trabalha
├── tests/             o árbitro comum — não altere
├── prompts/           registro do que foi pedido à IA
└── evidencias/        registro do que aconteceu ao executar
```

Rodar apenas um laboratório:

```bash
uv run pytest labs/lab-01-validador-senha
```

## Para o professor: como acrescentar um laboratório

1. Copiar a estrutura acima em `labs/lab-NN-nome/`.
2. Acrescentar o `src` do novo lab em `pythonpath`, no `pyproject.toml` da raiz.
3. Escrever `ESPECIFICACAO.md` com requisitos e critérios de aceitação rastreáveis.
4. Escrever os testes e **verificar nos dois estados**: vermelho no esqueleto, verde
   numa implementação de referência mantida fora do repositório público.
5. Escrever o `AGENTS.md` do laboratório.
6. Acrescentar a linha na tabela acima.

## Laboratórios de navegador

O Lab 02 usa JavaScript nativo e suíte executável no navegador, sem dependências npm.
Não precisa entrar no pythonpath. Seu tutorial documenta os comandos próprios e a
validação vermelha/verde, mantendo a referência fora do repositório público.
