# Evidência — Incremento 1: emitir senha

## Alteração

Em `src/fila.js`, a função `emitirSenha` passou a adicionar a senha corrente ao fim
da fila, incrementar `proximaSenha` e retornar a senha emitida. As demais operações
pendentes não foram alteradas.

## Verificação

Comando executado:

```text
node labs/lab-02-fila-facil/tests/executar.mjs
```

Resultado real:

```text
10 aprovados · 14 falhas · 24 testes
```

As quatro verificações diretas de RF-02 passaram. As falhas restantes são causadas
pelas funções `chamarProxima` e `reiniciarFila`, ainda pendentes nesta etapa.

## O que entendi do código

`proximaSenha` representa o próximo número ainda não emitido. A operação primeiro
guarda esse valor, coloca-o no fim de `aguardando` e só então avança a numeração; por
isso a senha retornada é a mesma senha que entra na fila.
