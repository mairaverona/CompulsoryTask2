from django.urls import path
from . import views

app_name = 'bookClub'

urlpatterns = [
    path('', views.index, name='index'),  # Root URL pattern
    path('register/success/', views.successful_reg, name='successful_reg'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),  # Add this line for login
    path('currently_reading/', views.currently_reading, name='currently_reading'),
    path('next_read/', views.next_read, name='next_read'),
    path('past_weeks/', views.past_weeks, name='past_weeks'),
]
