# from locale import NOEXPR
from .models import advanceFcompany, uplaodingDocument
from admins.models import new_document, new_item, f_company
from django.views.generic import TemplateView, ListView,CreateView,DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse
from admins.models import new_document,new_item,f_company

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

#add advanced company
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

class DocumentView(view_document_permision,ListView):
    paginate_by = 5
    template_name = "user/documents-page.html"
    context_object_name = 'documents'

    def get_queryset(self):
        return self.request.user.documents.all()


class DeleteDocument(DeleteView):
    model = uplaodingDocument
    
    def get_success_url(self) -> str:
        return reverse('documents_page')
    



class AdvancedFcompanyrecordView(view_advanced_f_company_permision,ListView):
    queryset = advanceFcompany.objects.all()
    template_name = "user/advanced-f-company-report.html"
    context_object_name = "companies"


class FcompanyrecordView(view_f_company_permision,ListView):
    model = advanceFcompany
    paginate_by = 1
    template_name = "user/f-company-report.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['FCompany'] = advanceFcompany.objects.all()
        return ctx  

class SearchView(ListView):
    model = uplaodingDocument
    template_name = "user/search-or-uploading-page.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['DocumentType'] = new_document.objects.all()
        ctx['itemType'] = new_item.objects.all()
        return ctx 


#login page
class login_user(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self) -> str:
        return reverse('index')


