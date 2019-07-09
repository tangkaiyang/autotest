from django.db import models


# Create your models here.

class Set(models.Model):
    setname = models.CharField(max_length=64, verbose_name="系统名称")  # 设置名称
    setvalue = models.CharField(max_length=20, verbose_name="系统设置")  # 设置值

    class Meta:
        verbose_name = "系统设置"
        verbose_name_plural = "系统设置"

    def __str__(self):
        return self.setname
