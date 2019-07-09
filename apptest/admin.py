from django.contrib import admin
from .models import Appcase, Appcasestep


# Register your models here.

class AppcasestepAdmin(admin.TabularInline):
    list_display = ['appteststep', 'apptestobjname', 'appfindmethod', 'appevelment', 'appoptmethod', 'appassertdate',
                    'apptestresult', 'create_time', 'id', 'appcase']
    model = Appcasestep
    extra = 1


class AppcaseAdmin(admin.ModelAdmin):
    list_display = ['appcasename', 'apptestresult', 'create_time', 'id']
    inlines = [AppcasestepAdmin]


admin.site.register(Appcase, AppcaseAdmin)
