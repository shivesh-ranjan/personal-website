from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    projectId = models.AutoField
    projectName = models.CharField(max_length=255)
    projectDesc = models.CharField(max_length=555)
    projectDate = models.DateField(auto_now_add=True)
    projectGitHub = models.URLField(max_length=555)
    projectDeployed = models.URLField(max_length=555)
    projectPic = models.ImageField(upload_to='projectPics/')

    def __str__(self):
        return self.projectName

class BlogCategory(models.Model):
    blogCategory = models.CharField(max_length=255)

    def __str__(self):
        return self.blogCategory

class Blog(models.Model):
    blogId = models.AutoField
    blogAuthor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    blogName = models.CharField(max_length=255)
    blogDesc = RichTextField()
    blogDate = models.DateField(auto_now_add=True)
    blogPic = models.ImageField(upload_to='blogPics/')
    blogTag = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.blogName + " | " + str(self.blogAuthor)
