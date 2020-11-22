from django.contrib import admin

from .models import Project, Role, ProjectParticipant

admin.site.register(Role)
admin.site.register(Project)
admin.site.register(ProjectParticipant)
