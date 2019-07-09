from django.db import models


# from product.models import Product

# Create your models here.


class Appcase(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 管理产品ID
    appcasename = models.CharField(max_length=200, verbose_name="用例名称")  # 测试用例名称
    apptestresult = models.BooleanField(verbose_name="测试结果")  # 测试结果
    apptester = models.CharField(max_length=16, verbose_name="测试负责人")  # 执行人
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")  # 创建时间,自动获取当前时间

    class Meta:
        verbose_name = 'app测试用例'
        verbose_name_plural = 'app测试用例'

    def __str__(self):
        return self.appcasename


class Appcasestep(models.Model):
    Appcase = models.ForeignKey('Appcase', on_delete=models.CASCADE) # 关联接口ID
    appteststep = models.CharField(max_length=200, verbose_name="测试步骤") # 测试步骤
    apptestobjname = models.CharField(max_length=200, verbose_name="测试对象名称描述") # 测试对象名称描述
    appfindmethod = models.CharField(max_length=200, verbose_name="定位方式") # 定位方式
    appevelement = models.CharField(max_length=800, verbose_name="控件元素") # 控件元素
    appoptmethod = models.CharField(max_length=200, verbose_name="操作元素") # 操作方法
    apptestdata = models.CharField(max_length=200, null=True, verbose_name="测试数据") # 测试数据,临时增加字段时要设置可为空