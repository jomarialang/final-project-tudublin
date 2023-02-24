from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register/success', views.register_success, name='register_success'),
    path('activate/<uid64>/<token>', views.activate, name='activate')
]