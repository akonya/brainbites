from django.contrib import admin
from brainbites.bite.models import Tag, Author, Bite

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Bite)