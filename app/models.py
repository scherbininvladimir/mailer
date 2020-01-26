from django.db import models

class Message(models.Model):
    msg = models.TextField('Текст сообшения')
    delay = models.IntegerField('Отправить через (сек)')
    is_sent = models.BooleanField(default=False)
