import os
import io
import uuid

import pytest
from bddrest import status, response, given, when
from yhttp.core import text, json

from yhttp.ext.media import install


def test_extension(httpreq, app, tempdir, mocker):
    install(app)
    mediadirectory = os.path.join(tempdir, 'media')
    app.settings.media.physical = mediadirectory
    app.ready()

    assert app.media
    assert app.media.settings.physical == mediadirectory

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

        expected = os.path.join(mediadirectory, 'foos', expected_filename)
        assert os.path.exists(expected)

    with httpreq(verb='DELETE', form=dict(filename=expected_filename)):
        assert status == 200

        assert not os.path.exists(expected)
#
#         when(headers=given - 'Authorization')
#         assert status == 401
#
#         when(headers={'Authorization': 'mAlfoRMeD'})
#         assert status == 401
#
#         when(headers={'Authorization': 'Bearer mAlfoRMeD'})
#         assert status == 401
#
#     with httpreq('/admin', headers={'Authorization': f'Bearer {token}'}):
#         assert status == 200
#         assert response.json == ['admin']
#
#         when(headers={'Authorization': token})
#         assert status == 401
#
#         when()
#         assert status == 401
#
#         when()
#         assert status == 200
#
#         when(headers={'Authorization': f'Bearer {token}'})
#         assert status == 403
#
#         when(headers={'Authorization': f'Bearer {token}'})
#         assert status == 403
#
#     yapp.shutdown()
