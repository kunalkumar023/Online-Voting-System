from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('env',views.env,name="env"),
    path('vote/<str:pk>',views.vote,name="vote")
]
