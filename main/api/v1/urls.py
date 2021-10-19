from . import views
from django.urls import path

urlpatterns = [
    path('movie/', views.ProjectList.as_view()),
    path('movie/<int:pk>', views.ProjectDetail.as_view()),
    path('posts/', views.PostList.as_view()),
]