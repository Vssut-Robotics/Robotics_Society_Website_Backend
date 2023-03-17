
from django.urls import path
from src.views import member_views as views

urlpatterns = [
    path('', views.getMembers, name="members"),
    path('<str:pk>/', views.getMember, name="member"),
]
