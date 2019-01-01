from django.db import models
import time


class Category(models.Model):
    name = models.CharField(max_length=255,null=False)
    img = models.IntegerField()
    status = models.SmallIntegerField(default=1)
    pid = models.IntegerField(default=0)
    create_time = models.IntegerField(default=int(time.time()))
    update_time = models.IntegerField(default=int(time.time()))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dp_categories"

