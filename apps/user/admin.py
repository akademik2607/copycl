from django.contrib import admin

# Register your models here.
from apps.archives.models import ArchiveBase
from apps.user.models import CustomUser


class ArchiveUserInline(admin.TabularInline):
    model = ArchiveBase
    extra = 0


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    inlines = [ArchiveUserInline]
