from django.urls import path
from . import views
# from .views import register

urlpatterns=[
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout')

]