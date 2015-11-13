from django.contrib import admin
from models import *

class UserMessageAdmin(admin.ModelAdmin):
    list_display = ("email", )

admin.site.register(UserMessage, UserMessageAdmin)
