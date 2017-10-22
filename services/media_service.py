from flask import url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads, UploadNotAllowed


def get_image_path(path):
    if 'http://' in path:
        return path
    else:
        return url_for('static', filename=path)


class MediaService:
    __EXCEL = ('xlsx',)

    def __init__(self, app):
        self.app = app

        app.config["UPLOADED_PHOTOS_DEST"] = self.app.root_path + "/uploads/images"
        self.photos = UploadSet('photos', IMAGES)
        configure_uploads(app, self.photos)

        app.config["UPLOADED_EVENTS_DEST"] = self.app.root_path + "/uploads/events/"
        self.excel = UploadSet('events', self.__EXCEL)
        configure_uploads(app, self.excel)

    def uploadImage(self, photo):
        try:
            filename = self.photos.save(photo)
        except UploadNotAllowed:
            return None
        else:
            return self.photos.url(filename)

    def uploadExcel(self, doc):
        try:
            filename = self.excel.save(doc)
        except UploadNotAllowed:
            return None
        else:
            return "uploads/events/" + filename

