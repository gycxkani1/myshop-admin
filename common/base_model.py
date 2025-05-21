from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    '''抽象基类'''
    # create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    # update_time=models.DateTimeField(auto_now=True,verbose_name="更新时间")
    create_time=models.DateTimeField(default=timezone.now,verbose_name="创建时间")
    update_time=models.DateTimeField(default=timezone.now,verbose_name="更新时间")


    class Meta:
        #指定抽象基类
        abstract=True