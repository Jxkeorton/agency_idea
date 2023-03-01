from django.urls import path
from members import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_page, name='login_page')
]