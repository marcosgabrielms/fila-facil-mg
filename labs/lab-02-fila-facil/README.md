# Lab 02 — Fila Fácil

**Unidade 2 — Assistentes, agentes e ferramentas.** Uma aplicação de fila de recepção
para observar como um agente lê, edita, verifica e recebe intervenção humana.

Comece pelo **[Tutorial prático](TUTORIAL.md)**. Versão para leitura/impressão:
[Tutorial em PDF](Tutorial_Pratico_Lab_02_Fila_Facil.pdf).

## Executar, a partir da raiz do repositório

```bash
uv run python -m http.server 8000 --bind 127.0.0.1 -d labs/lab-02-fila-facil
```

- Aplicação: <http://127.0.0.1:8000/>
- Testes: <http://127.0.0.1:8000/tests/>

Alternativa sem servidor: abrir index.html e tests/index.html pelo gerenciador de arquivos.
Sem Node, npm, banco ou dependências JavaScript. Os dados vivem somente na aba.

## O exercício

A interface está pronta. Implemente três funções em `src/fila.js` conforme a
[especificação](ESPECIFICACAO.md), preservando os testes:

1. Emitir senhas sequenciais.
2. Chamar em ordem de chegada, preservando a última chamada quando a fila está vazia.
3. Reiniciar o estado após confirmação feita pela interface.

Esqueleto: **6 aprovados, 18 falhas**. Conclusão: **24 aprovados, 0 falhas**, mais roteiro
visual. Quem já tem Node 18+ pode usar `node labs/lab-02-fila-facil/tests/executar.mjs`
a partir da raiz. `uv run pytest` continua cobrindo apenas o Lab 01 Python.

Registre o processo em prompts/ e evidencias/. A solução de referência do professor
é mantida fora deste repositório. Depois do básico, veja [exercícios de evolução](EXERCICIOS.md).
