from django.contrib import admin
from thanks.models import *

class ThanksAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'name', )

    def get_name(self, obj):
        return obj.group.code
    get_name.short_description = 'Name'
    get_name.admin_order_field = 'group__name'


class GroupInfoInline(admin.StackedInline):
    model = GroupInfo
    extra = 3

class GroupAdmin(admin.ModelAdmin):
    list_display = ('code', )
    inlines = [GroupInfoInline]


class VThanksAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Group, GroupAdmin)
admin.site.register(Thanks, ThanksAdmin)
admin.site.register(VThanks, VThanksAdmin)