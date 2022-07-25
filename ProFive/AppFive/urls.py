from django.urls import path
from AppFive import views

app_name = 'AppFive'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login')
]
