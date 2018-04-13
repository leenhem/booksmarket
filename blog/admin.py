from django.contrib import admin
from blog.models import User,Book,Author
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)