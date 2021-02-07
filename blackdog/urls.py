from django.urls import path

from . import views

app_name = 'blackdog'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:bark_id>/', views.bark, name='bark'),
    path('<int:bark_id>/edit', views.edit, name='edit'),
]