from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, View, ListView,DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from  .models import ID_name, f_company, new_document, new_item, page_acces
from .mixins import AdminRequiredMixin
from .forms import UserForm, PagesAccessForm
from documents.models import uplaodingDocument
# Create your views here.

# admin login page

class Login(LoginView):
    template_name = 'admin/admin-login.html'

    def get_success_url(self) -> str:
        return reverse('admin_main')



# admin main page
class AdminMainView(AdminRequiredMixin, TemplateView):
    template_name = "admin/admin-main.html"


class AddUserView(AdminRequiredMixin, View):
    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            pages_form = PagesAccessForm(request.POST)
            if pages_form.is_valid():
                user.save()
                access = pages_form.save(commit=False)
                access.user = user
                access.admin = request.user
                access.save()
                messages.success(request, "User Created Successfuly.")
            else:
                messages.error(request, "some thing went wrong with pages.")
                for field in pages_form.errors:
                        messages.error(request, pages_form.errors[field].as_data()[0].message)
        else:
            messages.error(request, "Error in user details")
            for field in user_form.errors:
                    messages.error(request, user_form.errors[field].as_data()[0].message)

        return redirect('admin_main')


class AddDocTypeView(AdminRequiredMixin, View):
    def post(self, request):
        try:
            doc = new_document.objects.create(document=request.POST.get('document'))
            messages.success(request, f'doc type "{doc.document}" created successfuly.')
        except Exception as e:
            messages.error(request, e)
        return redirect('admin_main')


class AddItemView(AdminRequiredMixin, View):
    def post(self, request):
        try:
            item = new_item.objects.create(Item=request.POST.get('item'))
            messages.success(request, f'item "{item.Item}" created successfuly.')
        except Exception as e:
            messages.error(request, e)
        return redirect('admin_main')


class AddAdminView(AdminRequiredMixin, View):
    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request, "User Created Successfuly.")
        else:
            messages.error(request, "Error in user details")
            for field in user_form.errors:
                    messages.error(request, user_form.errors[field].as_data()[0].message)

        return redirect('admin_main')


class AddCompanyView(AdminRequiredMixin, View):
    def post(self, request):
        try:
            company = f_company.objects.create(company=request.POST.get('company'))
            messages.success(request, f'company "{company.company}" created successfuly.')
        except Exception as e:
            messages.error(request, e)
        return redirect('admin_main')


class AddIdView(AdminRequiredMixin, View):
    def post(self, request):
        try:
            id_ = ID_name.objects.create(id_key=request.POST.get('id'), name=request.POST.get("name"))
            messages.success(request, f'Id "{id_.name}" created successfuly.')
        except Exception as e:
            messages.error(request, e)
        return redirect('admin_main')

# admin account report
class AccountReportView(AdminRequiredMixin,ListView):
    template_name = "admin/admin-account-m-report.html"
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.annotate(documents_count=Count("documents")).filter(is_superuser=False)

class DocumentReportView(AdminRequiredMixin,ListView):
    template_name = "admin/admin-documents-report.html"
    context_object_name = "document"

    def get_queryset(self):
        return uplaodingDocument.objects.all()

class AdminDeleteAccount(DeleteView):
    model = User

    def get_success_url(self) -> str:
        return reverse('admin_account_report')

class AdminDeleteDocument(DeleteView):
    model = uplaodingDocument
    
    def get_success_url(self) -> str:
        return reverse('admin_documents_report')



# def admin_documents_report(request):
#     document = login.objects.all()
#     context = {'document': document}
#     return render(request, "admin/admin-documents-report.html" ,context)


# def delete(request,id):
#     customer = login.objects.filter(id=id)
#     customer.delete()
#     return render(request,'admin/admin-account-m-report.html')

