from django.urls import path
from . import views

urlpatterns = [
    path('user/list', views.user_list, name = 'user_list'),
    path('benefit/list', views.benefit_list, name = 'benefit_list'),
    path('benefit/user/add', views.benefit_add_user, name = 'benefit_add_user'),
]