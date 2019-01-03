from django.db import models
import time


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=60, unique=True)
    email = models.CharField(max_length=100, unique=True)
    email_code = models.CharField(max_length=255)
    email_type = models.SmallIntegerField()
    secret = models.CharField(max_length=255)
    status = models.SmallIntegerField(default=1)
    create_time = models.IntegerField(default=int(time.time()))
    update_time = models.IntegerField(default=int(time.time()))

    def __str__(self):
        return u'%s %s ' % (self.email, self.username)

    class Meta:
        db_table = "dp_users"
