from django.contrib import admin
from home.models import *


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', )


class MenuInfoInline(admin.StackedInline):
    model = MenuInfo
    extra = 3


class MenuAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'url', )
    inlines = [MenuInfoInline]


class SectionInline(admin.StackedInline):
    model = SectionInfo
    extra = 3


class SectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'basepage', )
    inlines = [SectionInline]


class BasePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'remark', )


admin.site.register(BasePage, BasePageAdmin)
admin.site.register(Languages, LanguageAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Section, SectionAdmin)