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

    def user(self, user_id):
        self.path = os.path.join(self.path, "users", str(user_id))
        return self

    def event(self, event_id):
        self.path = os.path.join(self.path, "events", str(event_id))
        return self

    def images(self):
        self.path = os.path.join(self.path, "images")
        return self

    def clear(self):
        self.path = ""


class Url:
    def __init__(self):
        self.path = ""

    def user(self, user_id):
        self.path += "users/" + str(user_id) + "/"
        return self

    def event(self, event_id):
        self.path += "events/" + str(event_id) + "/"
        return self

    def images(self):
        self.path += "images/"
        return self

    def clear(self):
        self.path = ""


class MediaService:
    __EXCEL = ('xlsx',)

    def __init__(self, app):
        self.app = app
        self.root = app.root_path
        self.uploads = app.config['UPLOAD_FOLDER']

    def uploadUserImage(self, image, user_id):
        try:

            filename = secure_filename(image.filename)

            path = Path().user(user_id).images().path
            path = os.path.join(self.root, self.uploads, path, filename)
            image.save(path)

        except:
            return None

        else:
            url = Url().user(user_id).images().path
            url = self.uploads + "/" + url + filename
            return url

    def uploadEventImage(self, image, event_id):
        pass
        # try:
        #     folder = Path().event(event_id).images().path
        #     filename = self.images.save(image, folder)
        # except UploadNotAllowed:
        #     return None
        # else:
        #     return self.images.url(filename)

    def removeUserImage(self, url, user_id):
        pass
        # try:
        #     image_name = url.split("/")[-1]
        #     folder = Path().user(user_id).images().path
        #     path = self.images.path(image_name, folder)
        #     os.remove(path)
        # except OSError:
        #     return None
        #
        # return image_name

    def removeEventImage(self, url, event_id):
        pass
        # try:
        #     image_name = url.split("/")[-1]
        #     folder = Path().event(event_id).images().path
        #     path = self.images.path(image_name, folder)
        #     os.remove(path)
        # except OSError:
        #     return None
        #
        # return image_name

    def uploadExcel(self, doc):
        pass
        # try:
        #     filename = self.excel.save(doc)
        # except UploadNotAllowed:
        #     return None
        # else:
        #     return "uploads/events/" + filename
