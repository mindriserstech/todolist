from django.contrib import admin

from .models import UserNote, UserTask
# Register your models here.
admin.site.register(UserNote)
admin.site.register(UserTask)