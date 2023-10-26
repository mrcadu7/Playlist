from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search_artists/', views.search_artists, name='search_artists'),
    path("", views.index, name="index"),
    path('add_to_playlist/', views.add_to_playlist, name='add_to_playlist'),
]
