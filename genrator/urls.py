
from django.urls import path
from genrator import views

urlpatterns = [
    path('home/',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('login/',views.user_login, name="login"),
    path('resume_builder/',views.resume_builder, name="resume_builder")
    
    
]