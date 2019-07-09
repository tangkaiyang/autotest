from django.db import models
from product.models import Product


# Create your models here.


class Bug(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 关联产品ID
    bugname = models.CharField(max_length=64, verbose_name="bug名称")  # Bug名称
    bugdetail = models.CharField(max_length=200, verbose_name="详情")  # 详情
    BUG_STATUS = (('激活', '激活'), ('已解决', '已解决'), ('已关闭', '已关闭'))
    bugstatus = models.CharField(max_length=200, choices=BUG_STATUS, default='激活', null=True,
                                 verbose_name="解决状态")  # 解决状态
    BUG_LEVEL = (('1', '1'), ('2', '2'), ('3', '3'))
    buglevel = models.CharField(max_length=200, null=True, choices=BUG_LEVEL, default='3', verbose_name='严重程度')  # 严重程度
    bugcreater = models.CharField(max_length=200, verbose_name="创建人")  # 创建人
    bugassign = models.CharField(max_length=200, verbose_name="分配给")  # 分配给
    created_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")  # 更新时间值

    class Meta:
        verbose_name = 'bug管理'
        verbose_name_plural = 'bug管理'

    def __str__(self):
        return self.bugname
