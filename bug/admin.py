from django.contrib import admin

from .models import Bug


# Register your models here.


class BugAdmin(admin.ModelAdmin):
    list_display = ['bugname', 'bugdetail', 'bugstatus', 'buglevel', 'bugcreater', 'bugassign', 'created_time', 'id']


admin.site.register(Bug, BugAdmin) # 把Bug管理模块注册到Django admin后台并能显示
