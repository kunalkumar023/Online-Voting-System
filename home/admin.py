from django.contrib import admin
from .models import data,Question,choice,Voter
# Register your models here.

admin.site.register(data)
admin.site.register(Question)
admin.site.register(choice)
admin.site.register(Voter)
