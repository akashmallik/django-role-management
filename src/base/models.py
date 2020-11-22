from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProjectParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.user.username } - { self.role.name } - { self.project.name }'
