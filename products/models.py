from django.db import models
from django.utils.text import slugify


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductColor(models.Model):
    color = models.CharField(max_length=100, verbose_name='رنگ')
    url_color = models.CharField(max_length=300, verbose_name='رنگ در url')

    def __str__(self):
        return f'{self.color}'

    class Meta:
        verbose_name = 'رنگ محصول'
        verbose_name_plural = 'لیست رنگ محصولات'


class ProductStyle(models.Model):
    style = models.CharField(max_length=100, verbose_name='استایل محصول')
    url_style = models.CharField(max_length=300, verbose_name='استایل در url')

    def __str__(self):
        return f'{self.style}'

    class Meta:
        verbose_name = 'استایل محصول'
        verbose_name_plural = 'لیست استایل محصولات'


class ProductTag(models.Model):
    tag = models.CharField(max_length=200, verbose_name='تگ')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ محصولات'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name='دسته بندی')
    pro_color = models.ManyToManyField(ProductColor, verbose_name='رنگ محصول')
    pro_style = models.ManyToManyField(ProductStyle, verbose_name='استایل محصول')
    pro_tag = models.ManyToManyField(ProductTag, verbose_name='تگ محصول')
    pro_pic = models.ImageField(upload_to='products/static/products/media', blank=True, null=True, verbose_name='تصویر محصول')
    title = models.CharField(max_length=150, verbose_name='عنوان محصول')
    price = models.IntegerField(verbose_name='قیمت')
    description = models.CharField(max_length=500, verbose_name='توضیحات')
    availability = models.BooleanField(verbose_name='موجود/ناموجود')
    count = models.IntegerField(verbose_name='تعداد محصول')
    slug = models.SlugField(default='', null=False, db_index=True, unique=True, verbose_name='عنوان در url')
    date = models.DateTimeField(verbose_name='تاریخ نوشته')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}---{self.price}'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
