from django.contrib import admin

#Не забыть поставить ограничение на админский ключ
from apps.archives.models import ArchiveBase, Key


class KeysInline(admin.TabularInline):
    model = Key
    extra = 0


@admin.register(ArchiveBase)
class ArchiveBaseAdmin(admin.ModelAdmin):
    inlines = [KeysInline]
