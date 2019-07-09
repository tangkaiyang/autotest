from django.db import models
from product.models import Product


# Create your models here.

class Apitest(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    # 关联产品ID,其中product是应用名,Product是product应用的表名
    apitestname = models.CharField(max_length=64, verbose_name='流程接口名称')  # 流程接口测试场景
    apitestdesc = models.CharField(max_length=64, null=True, verbose_name='描述')  # 流程接口描述
    apitester = models.CharField(max_length=16, verbose_name="测试负责人")  # 执行人
    apitestresult = models.BooleanField(verbose_name='测试结果')  # 流程接口测试结果
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")  # 创建时间,自动获取,当前时间

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'

    def __str__(self):
        return self.apitestname


class Apistep(models.Model):
    Apitest = models.ForeignKey('Apitest', on_delete=models.CASCADE)  # 关联接口ID
    apiname = models.CharField(max_length=100, verbose_name="接口名称")  # 接口标题
    apiurl = models.CharField(max_length=200, verbose_name="URL地址")  # 地址
    apistep = models.CharField(max_length=100, null=True, verbose_name="测试步骤")  # 测试步骤
    apiparamvalue = models.CharField(max_length=800, verbose_name="请求参数和值")  # 参数和值
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    apimethod = models.CharField(max_length=200, null=True, default='get', choices=REQUEST_METHOD,
                                 verbose_name="请求方法")  # 请求方法
    apiresult = models.CharField(max_length=200, verbose_name="预期结果")  # 预期结果
    apiresponse = models.CharField(max_length=5000, null=True, verbose_name="响应数据")  # 响应数据
    apiteststatus = models.BooleanField(verbose_name="是否通过")  # 测试结果
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")  # 创建时间,自动获取当前时间

    def __str__(self):
        return self.apiname


class Apis(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 关联产品id
    apiname = models.CharField(max_length=100, verbose_name="接口名称")  # 接口标题
    apiurl = models.CharField(max_length=200, verbose_name="url地址")  # 地址
    apiparamvalue = models.CharField(max_length=800, verbose_name='请求参数和值')  # 请求参数和值
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    apimethod = models.CharField(max_length=200, choices=REQUEST_METHOD, default='get', null=True,
                                 verbose_name="请求方法")  # 请求方法
    apitester = models.CharField(max_length=16, null=True, verbose_name="测试负责人")  # 执行人
    apiresult = models.CharField(max_length=200, verbose_name="预期结果")  # 逾期结果
    apiresponse = models.CharField(max_length=5000, null=True, verbose_name="响应数据")  # 响应数据
    apistatus = models.BooleanField(verbose_name="是否通过")  # 测试结果
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")  # 创建时间,自动获得当前时间

    class Meta:
        verbose_name = '单一场景接口'
        verbose_name_plural = '单一场景接口'

    def __str__(self):
        return self.apiname
