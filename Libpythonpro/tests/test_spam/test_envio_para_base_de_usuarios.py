from unittest.mock import Mock

import pytest

from Libpythonpro.spam.main import EnviadorDeSpam
from Libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Carlos', email='teste@python.com.br'),
            Usuario(nome='Juninho', email='teste1@python.com.br')
        ],
        [
            Usuario(nome='Carlos', email='teste@python.com.br')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'teste@python.com.br',
        'Curtso Pytools',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Carlos', email='teste@python.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'teste1@python.com.br',
        'Curtso Pytools',
        'Confira os módulos fantásticos'
    )

    enviador.enviar.assert_called_once_with(
        'teste1@python.com.br',
        'teste@python.com.br',
        'Curtso Pytools',
        'Confira os módulos fantásticos'
    )
