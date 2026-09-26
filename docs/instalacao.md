# Instalação

Você precisa de duas coisas: **Git** e **uv**. Só isso. Python não se instala à mão
nesta disciplina.

## Git

Confira se já tem:

```bash
git --version
```

Se não tiver: <https://git-scm.com/downloads>. No Windows, aceite as opções padrão do
instalador.

## uv

O `uv` gerencia a versão do Python e as dependências do projeto. Ele lê o
`.python-version` e o `uv.lock` deste repositório e monta o ambiente exato — o mesmo
para toda a turma. É isso que torna a comparação entre soluções justa.

**macOS e Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Feche e reabra o terminal. Confira:

```bash
uv --version
```

## Primeira execução

```bash
git clone https://github.com/aislanifpi/tec1053.git
cd tec1053
uv run pytest
```

A primeira vez demora: o `uv` baixa o Python 3.13 e as dependências. Depois é
instantâneo.

Testes vermelhos são o resultado correto — os laboratórios começam com a implementação
em aberto.

## Problemas comuns

**`uv: command not found` depois de instalar.** O terminal ainda tem o PATH antigo.
Feche e abra de novo. Se persistir, o instalador informa no fim da saída qual linha
acrescentar ao seu `~/.zshrc` ou `~/.bashrc`.

**Windows barra o script do PowerShell.** É política de execução. O comando acima já
inclui `-ExecutionPolicy ByPass` justamente para isso. Se ainda assim for bloqueado —
comum em máquina institucional gerenciada — use a rota em navegador descrita em
[`trilhas-de-ia.md`](trilhas-de-ia.md), que não exige instalação.

**Não tenho permissão de instalar nada no laboratório.** Mesma solução: rota em
navegador. Me avise para eu conferir se é o caso de toda a turma.

**Já tenho Python/Anaconda instalado, vai conflitar?** Não. O `uv` usa um Python próprio
e não mexe no que você já tem.

## Se nada funcionar

Fale comigo antes da aula, não durante. Problema de instalação não pode custar a sua
nota nem o tempo da turma.
