"""Implementação do validador de senha.

O contrato (`ResultadoValidacao`) já está definido e não deve ser alterado — os testes
dependem dele. O que falta é `validar_senha`.

Antes de escrever qualquer linha, leia `ESPECIFICACAO.md`. A seção 4 define maiúscula,
minúscula, dígito, caractere especial e espaço em branco de um jeito que não coincide
com o comportamento padrão dos métodos de `str` do Python. Isso é proposital.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ResultadoValidacao:
    """Resultado da validação de uma senha.

    Attributes:
        valida: ``True`` se e somente se ``erros`` estiver vazio.
        erros: códigos dos requisitos violados (``"RF-01"``, ``"RF-02"``, ...),
            em ordem crescente e sem repetição.
    """

    valida: bool
    erros: tuple[str, ...]


def validar_senha(senha: str) -> ResultadoValidacao:
    """Valida uma senha contra a política definida em ``ESPECIFICACAO.md``.

    Args:
        senha: a senha a validar, avaliada exatamente como recebida.

    Returns:
        O resultado da validação, com todos os requisitos violados.

    Raises:
        TypeError: se ``senha`` não for uma ``str``.
    """
    raise NotImplementedError(
        "Implemente esta função a partir de ESPECIFICACAO.md. "
        "Rode `uv run pytest` para ver quais critérios de aceitação ainda falham."
    )
