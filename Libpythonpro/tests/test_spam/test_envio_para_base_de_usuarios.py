from Libpythonpro.spam.enviador_de_email import Enviador
from Libpythonpro.spam.main import EnviadorDeSpam


def test_qtd_de_spam(sessao):
    enviador_de_spam= EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'carlos@gmail.com',
        'Curtso Pytools',
        'Confira os módulos fantásticos'
    )