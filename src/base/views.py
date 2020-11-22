import logging

from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView

from base.models import ProjectParticipant


logger = logging.getLogger('__base__')


class CustomPermissionMixin:

    def dispatch(self, request, *args, **kwargs):
        try:
            role = ProjectParticipant.objects.get(user=request.user).role.name
        except Exception as exc:
            logger.exception(exc)
        else:
            if role.lower() in self.allowed_roles:
                return super().dispatch(request, *args, **kwargs)
            else:
                raise PermissionDenied


class IndexView(CustomPermissionMixin, TemplateView):
    allowed_roles = ['manager', 'engineer']
    template_name = 'index.html'
