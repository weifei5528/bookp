from django.db import models
import time


class Config(models.Model):
    name = models.CharField(max_length=64, default='')
    title = models.CharField(max_length=32, default='')
    group = models.CharField(max_length=32, default='')
    type = models.CharField(max_length=32, default='')
    value = models.TextField(default='')
    options = models.TextField(default='')
    tips = models.CharField(max_length=255, default='')
    ajax_url = models.CharField(max_length=255, default='')
    next_items = models.CharField(max_length=255, default='')
    param = models.CharField(max_length=32, default='')
    format = models.CharField(max_length=32, default='')
    table = models.CharField(max_length=32, default='')
    level = models.SmallIntegerField(default=2)
    key = models.CharField(max_length=32, default='')
    option = models.CharField(max_length=32, default='')
    pid = models.CharField(max_length=32, default='')
    ak = models.CharField(max_length=32, default='')
    # 创建时间
    create_time = models.IntegerField(default=int(time.time()))
    # 最后的更新时间
    update_time = models.IntegerField(default=int(time.time()))
    sort = models.IntegerField(default=100)
    status = models.SmallIntegerField(default=1)

    def __str__(self):
        return u'%s %s ' % (self.name, self.title)

    class Meta:
        db_table = "dp_admin_config"
        ordering = ['sort']
