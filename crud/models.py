from django.db import models


class MyUser(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='телефон')

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'

    def __str__(self):
        return self.name
