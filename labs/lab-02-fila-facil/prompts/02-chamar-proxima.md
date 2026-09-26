# Incremento 2 — chamar próxima

Pedido do aluno: implementar somente `chamarProxima`, preservar `emitirSenha`, não
implementar `reiniciarFila`, executar a suíte, mostrar o diff e parar para revisão.

Implementação feita após autorização: retornar `null` sem alterar o estado quando a
fila estiver vazia; caso contrário, remover a primeira senha aguardando, defini-la
como atual, incrementar o total de chamadas e retorná-la.
