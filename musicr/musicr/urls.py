from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('add_to_playlist/', views.add_to_playlist, name='add_to_playlist'),
]
