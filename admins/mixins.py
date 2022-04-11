from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect


@method_decorator(login_required, name='dispatch')
class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser and request.user.is_staff):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
