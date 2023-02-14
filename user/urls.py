from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate_user, name='activate'),
    path('check-email/', views.check_email, name='check_email')
]
