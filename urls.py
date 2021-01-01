from django.urls import path
from . import views

urlpatterns = [
    path('', views.func_homepage, name='homepage'),
    path('contact/', views.func_contact, name='contact'),
    path('about/', views.func_about, name='about'),
    path('treatment/', views.func_treatment, name='treatment'),
    path('testimonials/', views.func_testimonials, name='testimonials'),
    path('gallery/', views.func_gallery, name='gallery'),
    path('ourteam/', views.func_ourteam, name='ourteam'),
    path('appointment/', views.func_appointment, name='appointment'),
]