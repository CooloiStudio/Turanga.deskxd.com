from django.contrib import admin
from models import *

class SpecialAdmin(admin.ModelAdmin):
    list_display = ("name", "img", )

class SectionHeaderAdmin(admin.ModelAdmin):
    list_display = ("gamename", "titleone", "titletwo", "img", )

class SectionOneAdmin(admin.ModelAdmin):
    list_display = ("gamename", "gametitle", "textone", "texttwo", "img", )

class SectionTwoAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "text", "img", "url", )

class SectionThreeAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "text", "img", "url", )

admin.site.register(Special, SpecialAdmin)
admin.site.register(SectionHeader, SectionHeaderAdmin)
admin.site.register(SectionOne, SectionOneAdmin)
admin.site.register(SectionTwo, SectionTwoAdmin)
admin.site.register(SectionThree, SectionThreeAdmin)
