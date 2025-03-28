from django.contrib import admin
import community.models as Models

# Register your models here.

for Model in Models:
    admin.site.register(Model)