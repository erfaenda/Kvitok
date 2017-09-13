from django.db import models

# Create your models here.
'''Класс характеризущий информационные таблицы'''
class InfoTable(models.Model):
    name = models.CharField(max_length=50, verbose_name='Информационные Таблицы')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'

    def __str__(self):
        return self.name

'''Класс характерезует конкретную запись таблицы, в нашем случае это запись квитка'''
class ZapisTable(models.Model):
    infotable = models.ForeignKey(InfoTable, on_delete=models.CASCADE, verbose_name='Информациялнные таблицы')
    name = models.CharField(default='Акт№ ', max_length=50, verbose_name='Акт№')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    invent_number = models.CharField(max_length=50, verbose_name='Инвентарный номер')
    name_host = models.CharField(max_length=50, verbose_name='Имя хоста')
    ipaddr = models.CharField(max_length=50, verbose_name='Ip адресс')
    ffrom = models.CharField(max_length=50, verbose_name='От кого')
    to = models.CharField(max_length=50, verbose_name='Кому')
    description = models.TextField(verbose_name='Примечание')


    class Meta:
        verbose_name = 'Квиток'
        verbose_name_plural = 'Квитки'
        ordering = ['name'] # сортировка по имени

    def __str__(self):
        return self.name