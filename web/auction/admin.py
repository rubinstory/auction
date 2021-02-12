from django.contrib import admin
from .models import Book, Person, BoardGame, Furniture, ETC
# Register your models here.

admin.site.register(Book)
admin.site.register(Person)
admin.site.register(BoardGame)
admin.site.register(Furniture)
admin.site.register(ETC)