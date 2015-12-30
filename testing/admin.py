from django.contrib import admin
from models import *

class UserMessageAdmin(admin.ModelAdmin):
    list_display = ("email", )


class PlatformAdmin(admin.ModelAdmin):
    list_display = ("code", )


class VersionInfoInline(admin.StackedInline):
    model = VersionInfo
    extra = 3


class VersionAdmin(admin.ModelAdmin):
    list_display = ('get_platform', 'versions', )
    inlines = [VersionInfoInline]

    def get_platform(self, obj):
        return obj.platform.code
    get_platform.short_description = 'Platform'
    get_platform.admin_order_field = 'platform__code'


class AvailableVersionAdmin(admin.ModelAdmin):
    list_display = ('get_platform', 'get_version', )

    def get_platform(self, obj):
        return obj.platform.code
    get_platform.short_description = 'Platform'
    get_platform.admin_order_field = 'platform__code'

    def get_version(self, obj):
        return obj.availableversion.versions
    get_version.short_description = 'Versions'
    get_version.admin_order_field = 'version__versions'



admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Versions, VersionAdmin)
admin.site.register(AvailableVersion, AvailableVersionAdmin)
