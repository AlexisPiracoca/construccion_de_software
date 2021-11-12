from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "universes"

urlpatterns = [
     path('',   views.list,   name="list_characters"),
     path('save', views.save, name="save_characters"),
     path('edit/<int:id>', views.edit, name='edit'),
     path('detail/<int:id>', views.detail, name="detail"),

]
