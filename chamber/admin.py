from django.contrib import admin
from . import models


# Register your models here.
class CaseAdmin(admin.ModelAdmin):
    list_display = ("title")


admin.site.register(models.Case)
