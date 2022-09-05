import pytest as pytest

from Libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['carlosarodrigues.05@gmail.com', 'foo@bar.com.br']

)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'Carlos',
        'Curso',
        'Primeira turma'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'Carlos']

)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'Carlos',
            'Curso',
            'Primeira turma'
        )
