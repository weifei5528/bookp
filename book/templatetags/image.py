from django import template
from book.models.attachment import Attachment as AttModel
register = template.Library()


@register.filter
def get_file_path(id):
    if id == 0:
        return None
    info = AttModel.objects.filter(id=id).all()[:1]
    if info is None:
        return None
    return info[0].path
