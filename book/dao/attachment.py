from book.models.attachment import Attachment as AttModel
from book.dao.common import Common


class Attachment(Common):
    def get_img(self, id):
        info = self.get_info(id)
        if info is None:
            return None
        return info.path

    def get_info(self, id):
        return AttModel.objects.filter(id=id).all()[:1]

