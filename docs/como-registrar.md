# Como registrar o processo

A disciplina avalia o **processo**, não só o código que passou nos testes. O registro é
o que torna o processo visível — e é o que sustenta três dos quatro pesos da avaliação.

## Onde

Dentro de cada laboratório:

```
labs/lab-NN-nome/
├── prompts/      o que você pediu à IA
└── evidencias/   o que aconteceu quando executou
```

As fichas em branco estão em [`../templates/`](../templates/).

## O que registrar

Em `prompts/`, um arquivo por interação **relevante** — a que mudou o código, mudou a
especificação ou mudou o seu entendimento do problema. Conversa de tira-dúvidas não
precisa entrar. Nomeie `NN-descricao-curta.md`.

Em `evidencias/`, um arquivo por sessão de trabalho, nomeado `AAAA-MM-DD-descricao.md`.

## Por que fica no Git

Porque o Git carimba data e autoria sozinho. Registro em documento solto pode ser
escrito na véspera da entrega; registro versionado, não. Isso protege quem trabalhou
de verdade.

## Honestidade do registro

Três coisas que tiram todo o valor do registro:

**Reescrever o prompt depois** para parecer mais inteligente. O valor está em ser fiel
ao que você realmente pediu.

**Apagar a tentativa que deu errado.** Tentativa fracassada costuma ensinar mais que a
que deu certo, e vale nota igual. O que não vale nota é fingir que ela não existiu.

**Preencher tudo no fim.** Registro feito de memória, três semanas depois, é ficção.

Evidência fabricada compromete a avaliação — está no plano de ensino. Mas o motivo real
para não fazer isso é outro: o registro é a sua defesa quando alguém perguntar se o
código é seu.

## A pergunta que decide tudo

A ficha de evidência termina com "o que eu entendi do código". Escreva com suas
palavras o que a solução faz.

Se você não consegue escrever essa seção, o código ainda não é seu. A defesa técnica
individual vai cobrar exatamente isso, e não há registro que substitua.

## Declaração de uso de IA

O plano de ensino exige que o uso de IA seja declarado. As fichas de `prompts/` já são
essa declaração — não há formulário separado. Quem não usou IA em um laboratório
registra isso também, numa linha.
