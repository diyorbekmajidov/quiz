from django.contrib import admin

# Register your models here.
from .models import Question,Quiz,User,Result,Result_detail,Option

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Result)
admin.site.register(Result_detail)
admin.site.register(Option)