from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('blog/',views.blog),
    path('about/',views.about),
    path('login/',views.login),
    ]




