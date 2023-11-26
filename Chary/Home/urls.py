
from django.contrib import admin
from django.urls import path
from Home import views;

admin.site.site_header = "CHARY ADMIN"
admin.site.site_title = " welcome chary"
admin.site.index_title = " Admin page"

urlpatterns = [
    path('', views.index,name="home"),
    path('home', views.index,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="about"),
    path('login',views.login,name="about"),
    path('contact',views.contact,name="contact"),
]