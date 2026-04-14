import os
import uuid


class Media:
    def configure(self, settings):
        self.settings = settings

    def save(self, field, entity):
        _, ext = os.path.splitext(field.filename)
        newname = f'{uuid.uuid4()}{ext}'
        directory = os.path.join(self.settings.directory, entity)
        if not os.path.exists(directory):
            os.mkdir(directory)

        fullname = os.path.join(directory, newname)
        with open(fullname, 'w+b') as w:
            w.write(field.file.read())

        return newname

    def delete(self, filename, entity):
        fullname = os.path.join(self.settings.directory, entity, filename)
        os.remove(fullname)
