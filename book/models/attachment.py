from django.db import models
import time


class Attachment(models.Model):
    uid = models.IntegerField(default=0)
    name = models.CharField(max_length=255, default='')
    module = models.CharField(max_length=32, default='')
    path = models.CharField(max_length=255, default='')
    thumb = models.CharField(max_length=255, default='')
    url = models.CharField(max_length=255, default='')
    mime = models.CharField(max_length=128, default='')
    ext = models.CharField(max_length=8, default='')
    size = models.IntegerField(default=0)
    md5 = models.CharField(max_length=32, default='')
    sha1 = models.CharField(max_length=40, default='')
    driver = models.CharField(max_length=16, default='')
    create_time = models.IntegerField(default=int(time.time()))
    update_time = models.IntegerField(default=int(time.time()))
    sort = models.IntegerField(default=100)
    status = models.SmallIntegerField(default=1)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dp_admin_attachment"

