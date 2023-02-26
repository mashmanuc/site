from django.db import models
class articls(models.Model):
    title=models.CharField('Назва',max_length= 50)
    anons=models.CharField('Анонс',max_length= 250)
    full_text=models.TextField('Стаття')
    data=models.DateField('Дата')
    
    def __str__(self):
        return   self.title
    
    class Meta:
        verbose_name='новина'
        verbose_name_plural='новини'