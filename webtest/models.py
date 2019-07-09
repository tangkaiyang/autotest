from django.db import models

from product.models import Product


# Create your models here.

class Webcase(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 关联产品ID
    webcasename = models.CharField(max_length=200, verbose_name="用例名称")  # 测试用例名称
    webtestresult = models.BooleanField(verbose_name="测试结果")  # 测试结果
    webtester = models.CharField(max_length=16, verbose_name="测试负责人")  # 执行人
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")  # 创建时间,自动获取当前时间

    class Meta:
        verbose_name = "web测试用例"
        verbose_name_plural = "web测试用例"

    def __str__(self):
        return self.webcasename


class Webcasestep(models.Model):
    Webcase = models.ForeignKey('Webcase', on_delete=models.CASCADE)  # 关联接口ID
    webcasename = models.CharField(max_length=200, verbose_name="测试用例标题")  # 测试用例标题
    webteststep = models.CharField(max_length=200, verbose_name="测试步骤")  # 测试步骤
    webtestobjname = models.CharField(max_length=200, verbose_name="测试对象名称描述")  # 测试对象名称描述
    webfindmethod = models.CharField(max_length=200, verbose_name="定位方式")  # 定位方式
    webevelement = models.CharField(max_length=800, verbose_name="控件元素")  # 控件元素
    weboptmethod = models.CharField(max_length=200, verbose_name="操作方法")  # 操作方法
    webtestdata = models.CharField(max_length=200, null=True, verbose_name="测试数据")  # 测试数据,临时增加字段时要设置可为空
    webtestresult = models.BooleanField(verbose_name="测试结果")  # 测试结果
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")  # 创建时间,自动获取当前时间

    def __str__(self):
        return self.webcasename
