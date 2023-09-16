from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.http import require_http_methods
from .models import Project, Blog

# Create your views here.
@require_http_methods(['GET'])
def index(request):
    allproj = Project.objects.order_by('projectDate')[:4]
    allblog = Blog.objects.order_by('blogDate')[:4]
    return render(request, 'core/index.html', {'allproj': allproj, 'allblog': allblog})

@require_http_methods(['GET'])
def projects(request):
    if request.method == 'GET':
        allproj = Project.objects.order_by('projectDate')
        return render(request, 'core/projects.html', {'allproj': allproj})

@require_http_methods(['GET'])
def blogs(request):
  if request.method == 'GET':
    allblog = Blog.objects.order_by('blogDate')
    return render(request, 'core/blogs.html', {'allblog': allblog})

@require_http_methods(['GET', 'POST'])
def gigachaddyProject(request):
    if request.method == 'GET':
        return HttpResponse("""<div id="body" class="container mx-auto max-w-2xl">
      <p class="text-yellow-200 font-extrabold font-mono mx-6 my-2 text-2xl">ADD PROJECT</p>
      <form hx-post="/gigachaddy/project/" hx-target="#body" hx-swap="outerHTML" class="px-2 py-4 grid grid-cols-1">
        <input type="text" name="projectName" value="Name" class="rounded-lg text-black m-2 p-2">
        <input type="text" name="projectDesc" value="Desc" class="rounded-lg text-black m-2 p-2">
        <input type="url" name="projectGitHub" value="GitHub" class="rounded-lg text-black m-2 p-2">
        <input type="url" name="projectDeployed" value="Deployed" class="rounded-lg text-black m-2 p-2">
        <button type="submit" class="rounded-lg bg-yellow-300 text-black m-2 p-2">Submit</button>
      </form>
    </div>""")
    elif request.method == "POST":
        name = request.POST.get("projectName", "")
        desc = request.POST.get("projectDesc", "")
        github = request.POST.get("projectGitHub", "")
        deployed = request.POST.get("projectDeployed", "")
        project = Project(projectName=name, projectDesc=desc, projectGitHub=github, projectDeployed=deployed)
        project.save()
        return HttpResponse("""<p class="font-mono font-extrabold max-w-md m-4 text-yellow-200">Submitted Successfully!</p>""")
