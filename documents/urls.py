from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path("documents-page/", views.DocumentView.as_view(),name="documents_page"),
    path('document/<pk>/delete/',views.DeleteDocument.as_view(),name ='delete_document'),
    path("login-user",views.login_user.as_view(),name="login_user"),
    path("upload-document",views.AdddocumentView.as_view(),name="upload_document"),
    path('create-advanced-f-company',views.AddadvancedFcompanyView.as_view(), name="create_advanced_f_company"),
    path("advanced-f-company-report",views.AdvancedFcompanyrecordView.as_view(),name="advanced_f_company_report"),
    path("f-company-report",views.FcompanyrecordView.as_view() ,name="f_company_report"),
    path("create-f-company-record",views.AddfcompanyrecordView.as_view(),name="create_f_company_record"),
    path('search-advanced-f-company/',views.Search_advanced_F_company.as_view(),name = 'search_advanced_f_company'),
    path('search-f-company',views.Search_F_company.as_view(),name='search_f_company'),

]