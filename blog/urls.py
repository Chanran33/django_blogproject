from django.urls import path
from .views import * #views.py의 모든 함수를 불러와라

urlpatterns = [
    path('<str:pk>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>',edit,name="edit"),
    path('update/<str:id>',update,name="update"),
    path('delete/<str:id>',delete,name="delete"),
]
