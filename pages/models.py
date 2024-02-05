from django.db import models
from django.utils import timezone


# Create your models here.
class ContactUs(models.Model):
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    name = models.CharField(max_length=300, verbose_name='نام')
    message = models.TextField(max_length=530, verbose_name='متن پیام')
    date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ نوشته')
    seen = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'
