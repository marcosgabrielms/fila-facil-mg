"""Suíte de verificação do validador de senha.

Cada teste corresponde a um critério de aceitação de `ESPECIFICACAO.md`, seção 6.
A rastreabilidade critério → teste é o que torna a especificação verificável, e é
avaliada no portfólio da Unidade 3.

Esta suíte é o árbitro comum do experimento comparativo: soluções produzidas por
modelos diferentes são julgadas pelos mesmos testes, sem alteração. Modificar um
teste para fazê-lo passar invalida a comparação — se você acredita que um teste
contradiz a especificação, abra uma issue em vez de editá-lo.
"""

import pytest

from validador_senha import ResultadoValidacao, validar_senha

# Senha de referência: satisfaz todos os requisitos.
# 12 caracteres, com maiúscula, minúscula, dígito e especial ASCII, sem espaços.
SENHA_VALIDA = "Abcdef1!ghij"


def test_ca01_senha_valida() -> None:
    """CA-01: senha que atende a tudo é aceita, sem erros."""
    resultado = validar_senha(SENHA_VALIDA)

    assert isinstance(resultado, ResultadoValidacao)
    assert resultado.valida is True
    assert resultado.erros == ()


@pytest.mark.parametrize(
    ("codigo", "senha", "motivo"),
    [
        ("RF-01", "Ab1!def", "sete caracteres, um a menos que o mínimo"),
        ("RF-02", "Ab1!" + "x" * 61, "65 caracteres, um a mais que o máximo"),
        ("RF-03", "abcdef1!ghij", "nenhuma maiúscula"),
        ("RF-04", "ABCDEF1!GHIJ", "nenhuma minúscula"),
        ("RF-05", "Abcdefg!hijk", "nenhum dígito"),
        ("RF-06", "Abcdef1ghijk", "nenhum caractere especial"),
        ("RF-07", "Abcde 1!ghij", "contém um espaço"),
    ],
)
def test_ca02_cada_requisito_isolado(codigo: str, senha: str, motivo: str) -> None:
    """CA-02: cada requisito violado isoladamente produz o seu próprio código.

    Cada senha deste teste viola exatamente um requisito. Se a implementação
    reportar códigos a mais, ela está rejeitando por motivo errado.

    RF-08 fica de fora deste teste por impossibilidade lógica: toda senha da lista
    de proibidas já viola outros requisitos (nenhuma delas tem maiúscula e
    caractere especial). Não existe senha que viole RF-08 e mais nada. A cobertura
    de RF-08 está nos testes de CA-08.
    """
    resultado = validar_senha(senha)

    assert resultado.valida is False, f"deveria ser inválida: {motivo}"
    assert resultado.erros == (codigo,), (
        f"esperava apenas {codigo} ({motivo}), veio {resultado.erros}"
    )


def test_ca03_multiplos_erros() -> None:
    """CA-03: todos os motivos são reportados, não só o primeiro.

    Este é o requisito que justifica a existência da função: a tela de cadastro
    precisa mostrar tudo de uma vez.
    """
    # "abc" — curta, sem maiúscula, sem dígito, sem especial.
    resultado = validar_senha("abc")

    assert resultado.valida is False
    assert set(resultado.erros) == {"RF-01", "RF-03", "RF-05", "RF-06"}


def test_ca03_string_vazia_nao_quebra() -> None:
    """CA-03: string vazia é entrada válida do ponto de vista de tipo.

    Deve retornar o conjunto completo de violações aplicáveis, não levantar exceção.
    """
    resultado = validar_senha("")

    assert resultado.valida is False
    assert set(resultado.erros) == {"RF-01", "RF-03", "RF-04", "RF-05", "RF-06"}


def test_ca04_erros_ordenados_sem_repeticao() -> None:
    """CA-04: a ordem é determinística e não há códigos repetidos."""
    # Duas maiúsculas ausentes não podem gerar RF-03 duas vezes; dois espaços
    # não podem gerar RF-07 duas vezes.
    resultado = validar_senha("ab  cd")

    assert list(resultado.erros) == sorted(resultado.erros), "erros fora de ordem"
    assert len(resultado.erros) == len(set(resultado.erros)), "códigos repetidos"


@pytest.mark.parametrize(
    ("senha", "codigo_esperado", "explicacao"),
    [
        ("çbcdef1!ghij", "RF-03", "Ç minúsculo não é maiúscula ASCII; falta maiúscula"),
        ("ÇBCDEF1!GHIJ", "RF-04", "nenhuma minúscula ASCII — Ç não conta"),
        ("Abcdefg!hij٣", "RF-05", "٣ é dígito Unicode, mas não é 0-9"),
        ("AbcdefgⅣhij!", "RF-05", "Ⅳ é numeral romano Unicode, não é dígito ASCII"),
    ],
)
def test_ca05_nao_ascii_nao_conta(
    senha: str, codigo_esperado: str, explicacao: str
) -> None:
    """CA-05: as classes de caractere são ASCII, conforme a seção 4.1.

    Implementações que usam `str.isupper()`, `str.islower()` ou `str.isdigit()`
    diretamente falham aqui — esses métodos seguem regras Unicode.
    """
    resultado = validar_senha(senha)

    assert codigo_esperado in resultado.erros, explicacao


def test_ca05_acentuada_nao_e_especial() -> None:
    """CA-05: caractere acentuado não pertence ao conjunto de especiais."""
    # Tem maiúscula, minúscula e dígito, mas o único candidato a "especial" é "é".
    resultado = validar_senha("Abcdef1éghij")

    assert "RF-06" in resultado.erros


@pytest.mark.parametrize(
    ("senha", "deve_violar_rf01", "deve_violar_rf02"),
    [
        ("Abcd1!gh", False, False),  # exatamente 8 — aceito
        ("Abcd1!g", True, False),  # 7 — curto demais
        ("Abcd1!" + "x" * 58, False, False),  # exatamente 64 — aceito
        ("Abcd1!" + "x" * 59, False, True),  # 65 — longo demais
    ],
)
def test_ca06_limites_inclusivos(
    senha: str, deve_violar_rf01: bool, deve_violar_rf02: bool
) -> None:
    """CA-06: os limites de 8 e 64 são inclusivos — erro clássico de off-by-one."""
    resultado = validar_senha(senha)

    assert ("RF-01" in resultado.erros) is deve_violar_rf01, (
        f"tamanho {len(senha)}: RF-01 avaliado errado"
    )
    assert ("RF-02" in resultado.erros) is deve_violar_rf02, (
        f"tamanho {len(senha)}: RF-02 avaliado errado"
    )


@pytest.mark.parametrize(
    ("branco", "nome"),
    [
        (" ", "espaço comum"),
        ("\t", "tabulação"),
        ("\n", "quebra de linha"),
        ("\r", "retorno de carro"),
        ("\v", "tabulação vertical"),
        (" ", "espaço inquebrável"),
    ],
)
def test_ca07_espacos_em_branco(branco: str, nome: str) -> None:
    """CA-07: qualquer forma de espaço em branco viola RF-07 (seção 4.3)."""
    resultado = validar_senha(f"Abcde1!{branco}fghi")

    assert "RF-07" in resultado.erros, f"não detectou {nome}"


def test_ca07_senha_nao_sofre_strip() -> None:
    """CA-07: a senha não é tratada antes de validar (seção 5).

    Uma implementação que aplica `strip()` deixaria de ver o espaço nas pontas
    e aceitaria esta senha.
    """
    resultado = validar_senha(" Abcdef1!ghij ")

    assert "RF-07" in resultado.erros


@pytest.mark.parametrize("senha", ["123456", "password", "qwerty", "senha123", "admin"])
def test_ca08_senhas_proibidas(senha: str) -> None:
    """CA-08: a lista da seção 4.4 é rejeitada por RF-08."""
    resultado = validar_senha(senha)

    assert "RF-08" in resultado.erros


@pytest.mark.parametrize("senha", ["PASSWORD", "Password", "PaSsWoRd", "ADMIN"])
def test_ca08_proibidas_ignoram_caixa(senha: str) -> None:
    """CA-08: a comparação ignora maiúsculas e minúsculas."""
    resultado = validar_senha(senha)

    assert "RF-08" in resultado.erros


@pytest.mark.parametrize("senha", ["Password1!", "Xqwertyz9#", "Admin123!"])
def test_ca08_proibidas_sao_igualdade_nao_substring(senha: str) -> None:
    """CA-08: conter uma senha proibida não é o mesmo que ser uma.

    O oposto — tratar como substring — é um erro comum e rejeitaria senhas legítimas.
    """
    resultado = validar_senha(senha)

    assert "RF-08" not in resultado.erros


@pytest.mark.parametrize("entrada", [None, 123, 12.5, ["Abcdef1!ghij"], b"Abcdef1!"])
def test_ca09_tipo_invalido(entrada: object) -> None:
    """CA-09: entrada que não é `str` levanta TypeError (seção 5)."""
    with pytest.raises(TypeError):
        validar_senha(entrada)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "senha",
    [
        SENHA_VALIDA,
        "",
        "abc",
        "senha123",
        " Abcdef1!ghij ",
        "Abcd1!gh",
        "A" * 100,
        "Çé٣Ⅳ",
    ],
)
def test_ca10_coerencia_valida_erros(senha: str) -> None:
    """CA-10: `valida` é True se e somente se `erros` estiver vazio.

    Invariante do contrato. Vale para qualquer entrada, válida ou não.
    """
    resultado = validar_senha(senha)

    assert resultado.valida is (len(resultado.erros) == 0)


def test_ca10_resultado_e_imutavel() -> None:
    """CA-10: o resultado é um dataclass congelado — não deve ser alterável."""
    resultado = validar_senha(SENHA_VALIDA)

    with pytest.raises(Exception):  # noqa: B017 — FrozenInstanceError herda de Exception
        resultado.valida = False  # type: ignore[misc]
