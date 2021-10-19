from rest_framework import generics
from main.models import Project, Post
from .serializers import ProjectsListSerializers, ProjectDetailSerializer, PostListSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsListSerializers

class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['prise', 'created_at']
    filterset_fields = ['category']