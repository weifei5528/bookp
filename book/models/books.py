from django.db import models
import time


class Books(models.Model):
    # 名称
    name = models.CharField(max_length=100)
    # 图片的id
    img = models.IntegerField(null=True)
    # 点击次数
    click = models.IntegerField()
    # 作者
    author = models.CharField(max_length=100, default='未知')
    # 出版社
    publish = models.CharField(max_length=255, default='未知')
    # 来源
    from_to = models.CharField(max_length=255, null=True, db_column="from")
    # 描述
    description = models.TextField()
    # 创建时间
    create_time = models.IntegerField(default=int(time.time()))
    # 最后的更新时间
    update_time = models.IntegerField(default=int(time.time()))
    # 状态
    status = models.SmallIntegerField(default=1)
    # 类型
    type = models.SmallIntegerField(default=2)
    # 分类的id
    cat_id = models.IntegerField()

    def __str__(self):
        return u'%s %s ' % (self.name, self.description)

    class Meta:
        db_table = "dp_books"
        ordering = ['create_time']

