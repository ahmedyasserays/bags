# from locale import NOEXPR
from operator import mod
from urllib import request
from django.http import QueryDict
from .models import advanceFcompany, uplaodingDocument
from admins.models import new_document, new_item, f_company
from django.views.generic import TemplateView, ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django_filters.views import FilterView
from admins.models import new_document,new_item,f_company
from .filters import Company_filter,document_filter
from .mixins import *



#the home page
class index(TemplateView):
    template_name = "index.html"

#uploading a document page
class AdddocumentView(upload_document_permision,CreateView):
    model = uplaodingDocument
    fields = ('documentNumber','itemType','documentDate','DocumentType','file')
    template_name = 'user/upload-document.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['DocumentType'] = new_document.objects.all()
        ctx['itemType'] = new_item.objects.all()
        ctx['success'] = self.request.session.pop('success', False)
        return ctx

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        self.request.session['success'] = True
        return reverse('upload_document')

#add f company
class AddfcompanyrecordView(upload_Fcompany_permision,CreateView):
    model = advanceFcompany
    fields =('date','FCompany','depositeAmount','paymentAmount','DepPayDate','NetAmount','details')
    template_name = 'user/create-f-company-record.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['FCompany'] = f_company.objects.all()
        ctx['success'] = self.request.session.pop('success', False)
        return ctx

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        self.request.session['success'] = True
        return reverse('create_f_company_record')

#update f company
class update_f_company(view_f_company_permision,UpdateView):
    model = advanceFcompany
    fields =('date','FCompany','depositeAmount','paymentAmount','DepPayDate','NetAmount','details')
    template_name = 'user/find-f-company.html'

    def form_invalid(self, form):
        print(form.errors)

        return super().form_invalid(form)   
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        print('success')
        return reverse('find_f_company')

#search in advanced f company
class Search_advanced_F_company(view_advanced_f_company_permision,CreateView):
    model = advanceFcompany
    fields = '__all__'
    template_name = 'user/search-advanced-f-company-record.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['FCompany'] = f_company.objects.all()
        return ctx

#search in f company
class Search_F_company(view_advanced_f_company_permision,CreateView):
    model = advanceFcompany
    fields =('date','FCompany','depositeAmount','paymentAmount','DepPayDate','NetAmount','details')
    template_name = 'user/search-f-company-record.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['FCompany'] = f_company.objects.all()
        return ctx

#add advanced f company
class AddadvancedFcompanyView(upload_advancedFcompany_permision,CreateView):
    model = advanceFcompany
    fields = ('date','idComapny','name','recevingNumber','receivingAmount','expenceNumber','expenceAmount','depositeAmount','paymentAmount','DepPayDate','FCompany','RecLink','NetAmount','receiDepPay','details','notes')
    template_name = 'user/create-advanced-f-company-record.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['FCompany'] = f_company.objects.all()
        ctx['success'] = self.request.session.pop('success', False)
        return ctx

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        self.request.session['success'] = True
        return reverse('create_advanced_f_company')

#show documents
class DocumentView(view_document_permision,FilterView):
    paginate_by = 5
    template_name = "user/documents-page.html"
    context_object_name = 'documents'
    filterset_class = document_filter

    def get_queryset(self):
        return self.request.user.documents.all()

#f company search filter
class F_company_find(view_f_company_permision,FilterView):
    paginate_by = 1
    queryset = advanceFcompany.objects.all()
    template_name = "user/find-f-company.html"
    context_object_name = "companies"
    filterset_class = Company_filter

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['FCompany'] = f_company.objects.all()
        ctx['fcompanies'] = advanceFcompany.objects.all()
        ctx['success'] = self.request.session.pop('success', False)
        return ctx
    
    def get_success_url(self) -> str:
        return reverse('find_f_company')


class Find_document(FilterView):
    queryset = uplaodingDocument.objects.all()
    template_name = 'user/find document.html'
    context_object_name = 'documents'
    filterset_class = document_filter

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['DocumentType'] = new_document.objects.all()
        ctx['itemType'] = new_item.objects.all()
        return ctx


#delete documents
class DeleteDocument(DeleteView):
    model = uplaodingDocument
    
    def get_success_url(self) -> str:
        return reverse('documents_page')
    
#show advanced f companies
class AdvancedFcompanyrecordView(view_advanced_f_company_permision,FilterView):
    queryset = advanceFcompany.objects.all()
    template_name = "user/advanced-f-company-report.html"
    context_object_name = "companies"
    filterset_class = Company_filter

#show f companies
class FcompanyrecordView(view_f_company_permision,FilterView):
    queryset = advanceFcompany.objects.all()
    template_name = "user/f-company-report.html"
    context_object_name = "FCompany"
    filterset_class = Company_filter

#login page
class login_user(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self) -> str:
        return reverse('documents_page')


