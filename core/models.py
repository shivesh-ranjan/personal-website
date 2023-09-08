from django.db import models

# Create your models here.
class Project(models.Model):
    projectId = models.AutoField
    projectName = models.CharField(max_length=255)
    projectDesc = models.CharField(max_length=555)
    projectDate = models.DateField(auto_now_add=True)
    projectGitHub = models.URLField(max_length=555)
    projectDeployed = models.URLField(max_length=555)

    def __str__(self):
        return self.projectName