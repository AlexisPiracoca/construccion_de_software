from . import views
from django.urls import path

app_name = "wines"

urlpatterns = [
     path('',   views.list,   name="list_wines"),
     path('save', views.save, name="save_wines"),
     
]