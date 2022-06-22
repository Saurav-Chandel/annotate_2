from secrets import choice
from django.contrib import admin
from .models import *
# Register your models here.



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question_text', 'was_published_recently',)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(Book)
admin.site.register(Car)