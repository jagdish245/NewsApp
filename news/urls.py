from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('preferences/', views.preferences, name='preferences'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]