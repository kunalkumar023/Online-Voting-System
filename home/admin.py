from django.contrib import admin
from .models import data,Question,choice
# Register your models here.

admin.site.register(data)
admin.site.register(Question)
admin.site.register(choice)
