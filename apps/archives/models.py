import uuid

from django.db import models

from apps.user.models import CustomUser

NULLABLE = {
    'null': True,
    'blank': True
}


def user_directory_path(instance, filename):

    return "user_{0}/{1}".format(instance.user.id, instance.name)


class ArchiveBase(models.Model):
    name = models.CharField('Название базы', max_length=125, **NULLABLE)
    user = models.ForeignKey(CustomUser, verbose_name='Владелец', on_delete=models.CASCADE)
    archive = models.FileField(verbose_name='Файл архива для базы', upload_to="uploads/%Y/%m/%d/", **NULLABLE)
    last_data = models.CharField('Дата создания файла конфига', max_length=200, **NULLABLE)
    admin_key = models.ForeignKey('Key', verbose_name='Администратор базы', on_delete=models.SET_NULL, **NULLABLE)


class Key(models.Model):
    archive_base = models.ForeignKey(ArchiveBase, on_delete=models.CASCADE)
    access_key = models.UUIDField('Ключ доступа', default=uuid.uuid4, editable=False, unique=True)
    hwid = models.CharField('HWID', max_length=25, **NULLABLE)
    is_active = models.BooleanField('Активен', default=True)
    created_at = models.DateTimeField('Время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)
