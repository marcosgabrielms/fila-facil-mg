# Evidência — Incremento 3: reiniciar fila

## Alteração

Em `src/fila.js`, a função `reiniciarFila` passou a restaurar no objeto recebido os
quatro campos do estado inicial: próxima senha 1, espera vazia, senha atual ausente e
zero chamadas.

## Verificação

Comando executado:

```text
node labs/lab-02-fila-facil/tests/executar.mjs
```

Resultado real:

```text
24 aprovados · 0 falhas · 24 testes
```

## O que entendi do código

O reinício substitui os valores dos campos já existentes, em vez de retornar um novo
estado. Assim, qualquer parte da interface que já mantenha referência ao objeto passa
a enxergar o estado reiniciado. A confirmação de reinício continua sendo responsabilidade
da interface fornecida.
