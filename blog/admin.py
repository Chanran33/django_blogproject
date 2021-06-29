from django.contrib import admin
from .models import Blog #models.py에 Blog를 등록해줬다고 알려줘야 한다.

# Register your models here.
admin.site.register(Blog)