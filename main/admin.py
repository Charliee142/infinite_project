from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Project,  ProjectAdmin)
admin.site.register(Contact)
