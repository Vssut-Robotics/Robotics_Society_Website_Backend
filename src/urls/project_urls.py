
from django.urls import path
from src.views import project_views as views

urlpatterns = [
    path('', views.getProjects, name="projects"),
    path('<str:pk>/', views.getProject, name="project"),
]
