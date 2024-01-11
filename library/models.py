from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 56)
    category = models.CharField(max_length = 56)
    author = models.CharField(max_length = 56)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'Books'

    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length= 56)
    slug = models.SlugField()
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = 'Category'

    def __str__(self) -> str:
        return self.name
    
class Readers(models.Model):
    name = models.CharField(max_length= 56)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Readers"
        db_table = 'Readers'
    
class BookRecord(models.Model):
    user = models.ForeignKey(Readers, on_delete= models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    day = models.PositiveIntegerField()

    class Meta:
        db_table = 'BookRecord'