"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from main import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.nothing),
    path('home/', views.home, name='home'),
    path('reverse/', views.reverse, name='reverse'),
    path('projects/', views.ProjectList.as_view(), name='projects'),
    path('projects-delete/<int:pk>', views.ProjectDelete.as_view(), name='project_delete'),
    path('project/<int:pk>', views.project_detail, name='project_detail'),
    path('posts/<int:pk>', views.category_posts, name='category_posts'),
    path('posts/del/<int:pk>', views.post_delete, name='post_delete'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('create_post', views.CreatePost.as_view(), name='create_post'),
    path('update_post/<int:pk>', views.PostUpdate.as_view(), name='update_post'),


]
