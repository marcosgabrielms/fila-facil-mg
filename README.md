# TEC.1053 — Tópicos Especiais em Programação

Repositório-base da disciplina **Tópicos Especiais em Programação** (TEC.1053),
Tecnologia em Análise e Desenvolvimento de Sistemas, IFPI — Campus Teresina Central,
2026/2.

Tema: desenvolvimento de software assistido por IA — modelos, especificações e
ferramentas.

> **A fórmula da disciplina:** resultado = modelo × contexto × ferramentas × verificação.
> O modelo é variável. O fluxo verificável é o objeto comum de aprendizagem.

## Comece aqui

### 1. Instale o `uv`

É a única coisa que você precisa instalar. Não instale Python — o `uv` cuida disso.

**macOS e Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Feche e reabra o terminal depois de instalar. Detalhes e problemas comuns em
[`docs/instalacao.md`](docs/instalacao.md).

### 2. Clone e rode os testes

```bash
git clone https://github.com/aislanifpi/tec1053.git
cd tec1053
uv run pytest
```

Na primeira execução o `uv` baixa o Python 3.13 e o pytest. Depois é instantâneo.

### 3. Veja tudo vermelho

É o esperado. Os laboratórios começam com a implementação em aberto — esse é o
exercício. Cada teste que falha aponta um critério de aceitação a cumprir.

## Laboratórios

O índice fica em [`labs/README.md`](labs/README.md). Comece pelo
[Lab 01 — Validador de senha](labs/lab-01-validador-senha/).

Já disponível: **[Lab 02 — Fila Fácil](labs/lab-02-fila-facil/)**, aplicação de fila
com HTML, CSS e JavaScript. [Tutorial prático](labs/lab-02-fila-facil/TUTORIAL.md).
Seus 24 testes rodam no navegador; `uv run pytest` continua coletando apenas o Lab 01.

Laboratórios novos aparecem ao longo do semestre. Para receber os que forem
adicionados depois do seu fork:

```bash
git remote add upstream https://github.com/aislanifpi/tec1053.git
git pull upstream main
```

Antes de atualizar, confira `git status --short` e preserve seu trabalho. Atualizações
podem conflitar em arquivos compartilhados. Se houver dúvida, use um clone novo,
como explicado no tutorial do Lab 02.

## Estrutura

```
docs/         guias: instalação, trilhas de IA, como registrar o processo
labs/         um diretório por laboratório, autocontido
templates/    fichas em branco e modelo de relatório comparativo
AGENTS.md     regras do repositório para agentes de IA
```

## Ferramentas de IA

Você pode usar qualquer ferramenta: Codex, Claude Code, OpenCode, Antigravity, Copilot,
ou o chat do navegador. Também pode não usar nenhuma. O que a disciplina exige é que o
uso seja **declarado** e **registrado**.

Os caminhos disponíveis, inclusive os gratuitos, estão em
[`docs/trilhas-de-ia.md`](docs/trilhas-de-ia.md).

O arquivo `AGENTS.md` é lido automaticamente por várias dessas ferramentas e já contém
as regras do repositório. Existe um geral na raiz e um específico por laboratório —
abrir e entender os dois é conteúdo da Unidade 3, não burocracia.

### Se você não tem acesso a nenhuma ferramenta paga

Você não precisa de nenhuma. Modelos pequenos rodando na sua própria máquina dão conta
dos laboratórios, e há rotas em navegador sem instalação.

### Se a sua máquina é fraca, ou você não tem máquina

Também há caminho. Fale comigo se o seu caso não estiver contemplado — resolvemos antes
de virar problema de nota.

## Como o trabalho é avaliado

A nota olha para **processo e evidências**, não para o tamanho do modelo nem para a
velocidade do computador. Máquina modesta não prejudica ninguém. Ferramenta paga não dá
vantagem.

O que pesa: a clareza da especificação que você produz, a rastreabilidade entre critério
e teste, a qualidade do registro em `prompts/` e `evidencias/`, e a sua capacidade de
**explicar e defender** o código. Código que você não consegue explicar não conta como
seu — vale para código escrito por IA e para código copiado de qualquer outra fonte.

Como registrar: [`docs/como-registrar.md`](docs/como-registrar.md).

## Regra que vale para tudo

**Não altere os testes.** Eles são o árbitro comum: se cada pessoa ajustar a régua, a
comparação entre modelos perde o sentido. Se você acha que um teste contradiz a
especificação, abra uma issue — isso conta a favor, não contra.

## Licença

MIT. Veja [`LICENSE`](LICENSE).
