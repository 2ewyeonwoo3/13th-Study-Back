from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Hashtag)
admin.site.register(Like)
