from django.contrib import admin
from models import *

class DocAdmin(admin.ModelAdmin):
    list_display = ['title', 'language']
    list_filter = ['language',]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Doc, DocAdmin)

