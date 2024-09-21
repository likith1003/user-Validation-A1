from django.urls import path
from .views import *


urlpatterns = [
    path('register', register, name='register'),
    path('home', home, name='home'),
    path('demo', demo, name='demo'),
    path('login', login, name='login')
]
