from bddcli import Given, Application as CLIApplication, status, stderr, \
    stdout, when
from yhttp.core import Application

from yhttp.ext.media import install


_app = Application('0.1.0', 'foo')
install(_app)


def test_cli():
    cliapp = CLIApplication('example', 'tests.test_cli:_app.climain')
    with Given(cliapp, 'media --help'):
        assert status == 0
        assert stderr == ''
