from django.contrib import admin
from blog.models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Answer)