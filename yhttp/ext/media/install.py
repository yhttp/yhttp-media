from pymlconf import Meld

from .cli import MediaCLI
from .media import Media


DEFAULT_SETTINGS = '''
directory: media
'''


def install(app):
    app.cliarguments.append(MediaCLI)
    app.settings |= Meld(DEFAULT_SETTINGS, root='media')
    app.media = Media()

    @app.when
    def configure(app):
        app.media.configure(app.settings.media)
