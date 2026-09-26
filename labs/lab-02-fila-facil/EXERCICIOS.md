# Depois do fluxo básico — evoluções do Fila Fácil

Comece somente depois de comprovar os 24 testes e o roteiro visual do fluxo básico.
Preserve a versão básica em um commit. Crie uma branch, por exemplo:

    git switch -c lab02-prioridade

As evoluções autorizam mudanças na interface e na lógica necessárias ao novo contrato.
Os testes básicos permanecem preservados. Adicione verificações próprias em
`extensoes/`, sem reescrever a régua original. O professor orientará mudanças de contrato.
Não implemente tudo de uma vez.

## Desafio principal: prioridade administrativa

O professor define uma regra didática: há senhas comuns e prioritárias. Enquanto as
duas categorias tiverem pessoas aguardando, chamar no máximo duas prioritárias
consecutivas antes de uma comum. Dentro de cada categoria, respeitar a ordem de chegada.
Se só uma categoria estiver aguardando, atendê-la normalmente. Ao chamar uma comum ou
reiniciar a fila, zerar o contador de prioritárias consecutivas. Emitir uma senha
não zera esse contador. Senhas usam numeração global única, mesmo com categorias.

Exemplo: chegada C1, P2, P3, P4, C5. Chamada esperada: P2, P3, C1, P4, C5.
Esta é uma simulação de fila administrativa, não uma regra de triagem médica ou
uma afirmação sobre prioridades legais. Não coletar diagnósticos ou dados pessoais.

Antes de pedir código, entregar:

1. Especificação da evolução com formato das senhas e comportamento de emitirSenha(estado)
   sem categoria (deve continuar emitindo comum para preservar compatibilidade).
2. Casos com só comuns, só prioritárias, ambas, chegada entre chamadas e reinício.
3. Plano dos arquivos que mudarão e justificativa.
4. Evidências das novas verificações e da preservação do fluxo comum.

## Outras evoluções, uma por vez

- Histórico visual das cinco últimas chamadas, com atualização e reinício definidos.
- Botão de repetir chamada, sem retirar outra senha nem incrementar o total.
- Persistência local entre recargas, com explicação do que acontece ao reiniciar.
- Segundo guichê: primeiro especificar como evitar chamar a mesma senha duas vezes.

Para cada evolução, registrar requisito, critérios, alterações, verificações e uma
intervenção humana. Acrescentar funcionalidade sem definir comportamento não conclui o desafio.
