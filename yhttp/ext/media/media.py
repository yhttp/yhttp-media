import os
import uuid


class Media:
    def configure(self, settings):
        self.settings = settings
        if not os.path.exists(settings.physical):
            os.mkdir(settings.physical)

    def save(self, field, entity):
        _, ext = os.path.splitext(field.filename)
        newname = f'{uuid.uuid4()}{ext}'
        directory = os.path.join(self.settings.physical, entity)
        fullname = os.path.join(directory, newname)

        if not os.path.exists(directory):
            os.mkdir(directory)

        with open(fullname, 'w+b') as w:
            w.write(field.file.read())

        return newname

    def delete(self, filename, entity):
        fullname = os.path.join(self.settings.physical, entity, filename)
        os.remove(fullname)
