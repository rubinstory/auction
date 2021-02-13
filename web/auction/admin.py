from django.contrib import admin
from .models import Book, Person, BoardGame, Furniture, ETC
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'price']

class PersonAdmin(admin.ModelAdmin):
	list_display = ['student_id', 'name', 'major']

class BoardGameAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']

class FurnitureAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']

class ETCAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']

admin.site.register(Book, BookAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(BoardGame, BoardGameAdmin)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(ETC, ETCAdmin)