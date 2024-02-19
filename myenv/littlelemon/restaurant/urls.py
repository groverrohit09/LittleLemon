#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu/', views.MenuItemView.as_view()),
]
