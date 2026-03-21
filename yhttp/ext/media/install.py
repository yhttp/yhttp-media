from .cli import MediaCLI
from .media import Media


DEFAULT_SETTINGS = '''
physical: media
virtual: media
'''


def install(app):
    app.cliarguments.append(MediaCLI)
    cfg = app.settings.merge('media: {}')
    app.settings['media'].merge(DEFAULT_SETTINGS)
    app.media = Media()

    @app.when
    def ready(app):
        app.media.configure(app.settings.media)
