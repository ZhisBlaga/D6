from django.contrib import admin
from p_library.models import Book, Author, PublishingHouse, Friend



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(PublishingHouse)
class PublishingHouse(admin.ModelAdmin):
    pass

@admin.register(Book)
class Book(admin.ModelAdmin):
    pass

@admin.register(Friend)
class Friend(admin.ModelAdmin):
    pass