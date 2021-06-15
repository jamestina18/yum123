from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('api', views.api),
    path('login',views.login),
    path('signup', views.signup),
    path('new-user',views.new_user),
    path('login-member', views.login_member),
    path('feed_welcome', views.feed_welcome),
    path('must_be_looged',views.must_be_looged),
    path('logged', views.logged),
    path('logout', views.logout)
]