from django.contrib import admin
from thanks.models import *

class ThanksAdmin(admin.ModelAdmin):
    list_display = ('name', )

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )

class VThanksAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Group, GroupAdmin)
admin.site.register(Thanks, ThanksAdmin)
admin.site.register(VThanks, VThanksAdmin)