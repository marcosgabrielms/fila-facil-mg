# Evidência — Incremento 2: chamar próxima

## Alteração

Em `src/fila.js`, a função `chamarProxima` passou a verificar se há espera. Se a fila
estiver vazia, ela retorna `null` imediatamente. Caso haja senha aguardando, remove a
primeira, atualiza `atual`, incrementa `totalChamadas` e a retorna. `reiniciarFila`
permaneceu pendente.

## Verificação

Comando executado:

```text
node labs/lab-02-fila-facil/tests/executar.mjs
```

Resultado real:

```text
20 aprovados · 4 falhas · 24 testes
```

As quatro falhas restantes são de RF-05 e RF-07 e decorrem exclusivamente de
`reiniciarFila` ainda lançar `LAB02_PENDENTE`.

## O que entendi do código

`shift()` remove e retorna o primeiro item da lista, que é a regra FIFO necessária
para a fila. O retorno antecipado na fila vazia ocorre antes de qualquer escrita;
assim, a última senha atendida e todos os outros campos são preservados.
