from django.contrib import admin
from .models import Book, Category, Readers,  BookRecord

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ["created_at", 'name'],
        }

@admin.register(Readers)
class ReadersAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(BookRecord)
class BookRecordAdmin(admin.ModelAdmin):
    list_display = ("user", "book")