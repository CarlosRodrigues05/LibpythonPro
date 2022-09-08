from unittest.mock import Mock

import pytest

from Libpythonpro import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('CarlosRodrigues05')
    assert avatar_url == url


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/110562693?v=4'
    resp_mock.json.return_value = {
        'login': 'CarlosRodrigues05', 'id': 110562693,
        'avatar_url': url,
    }
    get_mock = mocker.patch('Libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar_integração():
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url


