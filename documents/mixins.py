from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect


@method_decorator(login_required, name='dispatch')
class upload_document_permision(object):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff or request.user.pages.upload):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class upload_Fcompany_permision(object):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff or request.user.pages.new_record):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class upload_advancedFcompany_permision(object):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff or request.user.pages.avanced_record):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class view_document_permision(object):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff or request.user.pages.documents):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class view_f_company_permision(object):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff or request.user.pages.company_report):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class view_advanced_f_company_permision(object):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff or request.user.pages.advanced_report):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)