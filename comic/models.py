from django.db import models

# Create your models here.


class Chapter(models.Model):
    # 章节名字
    chapter_name = models.CharField(max_length=20)
    # 一话的页数
    chapter_pages = models.IntegerField(blank=False, default=14)
    # 对应的话数
    chapter_number = models.IntegerField(blank=False)


    def __str__(self):
        return self.chapter_name
