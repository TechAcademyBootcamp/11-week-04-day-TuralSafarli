from django.contrib import admin
from bookapp.models import *

# Register your models here.
admin.site.register ([Book, Category,Author])
