from django.db import models
from django.contrib.auth.models import AbstractUser
import time


class User(AbstractUser):
    email_code = models.CharField(max_length=128, blank=True)
    email_type = models.SmallIntegerField(default=0)
    create_time = models.IntegerField(default=int(time.time()))
    update_time = models.IntegerField(default=int(time.time()))
    phone = models.IntegerFiel()

    class Meta:
        verbose_name = "用户"
        db_table = "dp_user"

    def __str__(self):
        return self.user.__str__()
