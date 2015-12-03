from django.contrib import admin
from models import *

class AgreementAdmin(admin.ModelAdmin):
    list_display = ("content", )

class PrivacyAdmin(admin.ModelAdmin):
    list_display = ("content", )

admin.site.register(Agreement, AgreementAdmin)
admin.site.register(Privacy, PrivacyAdmin)