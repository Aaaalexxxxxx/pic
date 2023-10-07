from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html

# Create your models here.
User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)
    #для пользователя, создающего объявление
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('изображение', null=True, blank=True, upload_to='advertisements/')
    def get_html_image(self):
     if self.image:
          return format_html('<img src="{url}" style="max-width:80px; max-height:80px"/>', url=self.image.url)

