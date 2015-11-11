from django.contrib import admin
from models import *

class AgreementAdmin(admin.ModelAdmin):
    list_display = ("content", )

admin.site.register(Agreement, AgreementAdmin)
