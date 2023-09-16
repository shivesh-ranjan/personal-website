from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Project, Blog
from django.views.generic import ListView, DetailView

class BlogHomeView(ListView):
  model = Blog
  template_name = 'core/blogs.html'

class BlogPostView(DetailView):
  model = Blog
  template_name = 'core/blogPost.html'

class ProjectHomeView(ListView):
  model = Project
  template_name = 'core/projects.html'

@require_http_methods(['GET'])
def index(request):
    allproj = Project.objects.order_by('projectDate')[:4]
    allblog = Blog.objects.order_by('blogDate')[:4]
    return render(request, 'core/index.html', {'allproj': allproj, 'allblog': allblog})