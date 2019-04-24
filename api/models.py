from django.db import models


class Photo(models.Model):
    place = models.CharField(max_length=250, verbose_name='Место')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    image = models.ImageField(upload_to='photos/', verbose_name='Фото')

    def __str__(self):
        return 'Фото:{}'.format(self.id)

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'
