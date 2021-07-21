from django.contrib import admin
from book.models import Note,Equation,TimeTable
# Register your models here.

admin.site.register(Note)
admin.site.register(Equation)
admin.site.register(TimeTable)