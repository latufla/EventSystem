import os

from flask import url_for
from werkzeug.utils import secure_filename


def get_image_path(path):
    if 'uploads' in path:
        return path
    else:
        return url_for('static', filename=path)


class Path:
    def __init__(self):
        self.path = ""
        self.url = ""

    def user(self, user_id):
        self.path = os.path.join(self.path, "users", str(user_id))
        self.url += "users/" + str(user_id) + "/"
        return self

    def event(self, event_id):
        self.path = os.path.join(self.path, "events", str(event_id))
        self.url += "events/" + str(event_id) + "/"
        return self

    def images(self):
        self.path = os.path.join(self.path, "images")
        self.url += "images/"
        return self

    def results(self):
        self.path = os.path.join(self.path, "results")
        self.url += "results/"
        return self

    def clear(self):
        self.path = ""
        self.url = ""


class MediaService:
    __EXCEL = ('xlsx',)

    def __init__(self, app):
        self.app = app
        self.root = app.root_path
        self.uploads = app.config['UPLOAD_FOLDER']

    def uploadUserImage(self, image, user_id):
        filename = secure_filename(image.filename)

        folder = Path().user(user_id).images()
        path = os.path.join(self.root, self.uploads, folder.path)
        if not os.path.exists(path):
            os.makedirs(path)

        path = os.path.join(path, filename)
        image.save(path)

        url = folder.url + filename
        return url_for(self.uploads, filename=url)

    def uploadEventImage(self, image, event_id):
        filename = secure_filename(image.filename)

        folder = Path().event(event_id).images()
        path = os.path.join(self.root, self.uploads, folder.path)
        if not os.path.exists(path):
            os.makedirs(path)

        path = os.path.join(path, filename)
        image.save(path)

        url = folder.url + filename
        return url_for(self.uploads, filename=url)

    def removeUserImage(self, url, user_id):
        try:
            filename = url.split("/")[-1]
            folder = Path().user(user_id).images()
            path = os.path.join(self.root, self.uploads, folder.path, filename)
            os.remove(path)
        except OSError:
            return None

        return filename

    def removeEventImage(self, url, event_id):
        try:
            filename = url.split("/")[-1]
            folder = Path().event(event_id).images()
            path = os.path.join(self.root, self.uploads, folder.path, filename)
            os.remove(path)
        except OSError:
            return None

        return filename

    def uploadEventResult(self, doc, event_id):
        filename = secure_filename(doc.filename)

        folder = Path().event(event_id).results()
        path = os.path.join(self.root, self.uploads, folder.path)
        if not os.path.exists(path):
            os.makedirs(path)

        path = os.path.join(path, filename)
        doc.save(path)

        return os.path.join(self.uploads, folder.path, filename)

    def removeEventResult(self, path):
        try:
            path = os.path.join(self.root, path)
            os.remove(path)
        except OSError:
            return None

        return path
