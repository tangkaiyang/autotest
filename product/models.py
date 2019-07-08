from django.db import models


# Create your models here.

class Product(models.Model):
    productname = models.CharField(max_length=64, null=False, verbose_name="产品名称")  # 产品名称
    producter = models.CharField(max_length=200, null=False, verbose_name="产品负责人")  # 产品负责人
    productdesc = models.CharField(max_length=200, null=False, verbose_name="产品描述")  # 产品描述
    create_time = models.DateTimeField(auto_now=True, null=False, verbose_name="创建时间")  # 创建时间,自动获取当前时间

    class Meta:
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'

    def __str__(self):
        return self.productname
