from django.core.exceptions import PermissionDenied, ObjectDoesNotExist, FieldDoesNotExist
from django.views.generic import TemplateView

from base.models import ProjectParticipant


class CustomPermissionMixin:

    def dispatch(self, request, *args, **kwargs):
        try:
            role = ProjectParticipant.objects.get(user=request.user).role.name
        except:
            raise PermissionDenied
        else:
            if role.lower() in self.allowed_roles:
                return super().dispatch(request, *args, **kwargs)
            else:
                raise PermissionDenied


class IndexView(CustomPermissionMixin, TemplateView):
    allowed_roles = ['manager', 'engineer']
    template_name = 'index.html'
