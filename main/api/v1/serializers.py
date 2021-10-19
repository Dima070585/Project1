from rest_framework import serializers
from main.models import Project, Post

class ProjectsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =('id', 'title', 'technology')

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class PostListSerializers(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only= True, slug_field= 'name')
    class Meta:
        model = Post
        fields =('title', 'prise', 'created_at', 'category')