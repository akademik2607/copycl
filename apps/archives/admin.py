from django.contrib import admin

#Не забыть поставить ограничение на админский ключ
from apps.archives.models import ArchiveBase, Key


class KeysInline(admin.TabularInline):
    model = Key
    readonly_fields = ['access_key']
    extra = 0


@admin.register(ArchiveBase)
class ArchiveBaseAdmin(admin.ModelAdmin):
    inlines = [KeysInline]
