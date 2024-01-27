from django.db import models

# Create your models here.

class News(models.Model):
  title = models.CharField(max_length=150, verbose_name='Name')
  content = models.TextField(blank=True, verbose_name='Content')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of Published')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)
  is_publish = models.BooleanField(default=True, verbose_name='Published?')
  category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

  def __str__(self) :
    return self.title
  
  class Meta:
    verbose_name = 'News'
    verbose_name_plural = 'News'
    ordering = ['-created_at']


class Category(models.Model):
  title = models.CharField(max_length=150, db_index=True, verbose_name='Name of Categoty')


  def __str__(self) :
    return self.title

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'
    ordering = ['title']

