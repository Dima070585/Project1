from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Project, Category, Post
from main.forms import PostForms
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy


# Create your views here.
def nothing(request):
    return render(request, 'main/task.html')
def about(request):
    return HttpResponse('about page')


def home(request):
    name = 'John Doe'
    return render(request, 'main/home.html')


def reverse(request):
    user_text = request.GET['usertext']
    words = user_text.split(' ')
    context = {
        'usertext': user_text,
        'reversedtext': user_text[::-1],
        'words': len(words)
    }

    return render(request, 'main/reverse.html', context)

class ProjectList(generic.ListView):
    queryset = Project.objects.all()
    template_name = 'main/projects.html'
    context_object_name = 'projects'

class ProjectDelete(generic.DeleteView):
    model = Project

    def get_success_url(self):
        return reverse_lazy('projects')

#def main_projects(request):
 #   projects = Project.objects.all()
  #  context = {
   #     'projects': projects,
#    }
 #   return render(request, 'main/projects.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'main/project_detail.html', {'project': project})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})

def category_posts(request, pk=0):
    if pk == 0:
        posts = Post.objects.order_by('-created_at')[:3]
    else:
        posts = Post.objects.filter(category_id=pk)

    category = Category.objects.all()


    context = {
        'categories': category,
        'posts': posts,
    }
    return render(request, 'main/posts.html', context)

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('category_posts', pk=0)

class CreatePost(generic.CreateView):
    template_name = 'main/create_post.html'
    form_class = PostForms

    def post(self, request, *args, **Kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')

class PostUpdate(generic.UpdateView):
    template_name = 'main/update_post.html'
    form_class = PostForms
    model = Post

    def get_success_url(self):
        return reverse_lazy('home')


#def create_post(request):
#    if request.method == 'POST':
 #       create_form = PostForms(request.POST, request.FILES)
  #      if create_form.is_valid():
   #         create_form.save()
    #        return redirect('home')

#    create_form= PostForms()
 #   return render(request, 'main/create_post.html', {'create_form': create_form})

#def update_post(request,pk):
    #