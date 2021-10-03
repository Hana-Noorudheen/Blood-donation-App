from django.urls import path
from . import views

urlpatterns = [
    path('',views.homelogin,name='homelogin'),
    path('add-donor',views.form,name='form'),
    path('display',views.display,name='display'),
    path('signup', views.signup,name='signup'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout')

]


    # path('homeregister',views.homeregister,name='homeregister'),
    # path('Homesignup',views.homesignup,name='homesignup'),
    # path('home',views.index,name='index'),