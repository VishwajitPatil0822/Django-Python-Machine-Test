from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    client_name = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_created_by',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    projects = models.ManyToManyField('Project', related_name='projects', blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.client_name


class Project(models.Model):
    project_name = models.CharField(max_length=30)
    user = models.ManyToManyField(User, related_name='user', blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_created_by',null=True, blank=True)

    def __str__(self):
        return self.project_name