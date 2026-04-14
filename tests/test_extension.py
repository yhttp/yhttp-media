import os
import io
import uuid

from bddrest import status

from yhttp.ext.media import install


def test_extension(httpreq, app, tmpdir, mocker):
    install(app)
    app.settings.media.directory = tmpdir
    app.ready()

    assert app.media

    @app.route()
    def post(req):
        app.media.save(req.files['foo'], 'foos')

    @app.route()
    def delete(req):
        app.media.delete(req.form['filename'], 'foos')

    mockuuid = '3301a833-f9c8-49d9-ac43-df96f6798e55'
    expected_filename = f'{mockuuid}.pdf'
    mocker.patch.object(uuid, 'uuid4', return_value=uuid.UUID(mockuuid))
    file = io.BytesIO(b'foobarbaz')
    file.name = 'foo.pdf'
    with httpreq(verb='POST', multipart=dict(foo=file)):
        assert status == 200

        expected = os.path.join(tmpdir, 'foos', expected_filename)
        assert os.path.exists(expected)

    with httpreq(verb='DELETE', form=dict(filename=expected_filename)):
        assert status == 200

        assert not os.path.exists(expected)
