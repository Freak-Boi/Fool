from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='IndexBlog'),
    path('boi/', views.boi, name='boi')
]