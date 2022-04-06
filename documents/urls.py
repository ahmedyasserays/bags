import imp
from unicodedata import name
from django import views
from django.urls import path,include
from documents import views
urlpatterns = [
    path('', views.index, name='index'),
    path("advanced-f-company-report",views.advanced_f_company_report, name='advanced_f_company_report'),
    path("documents-page", views.documents_page,name="documents_page"),

    # mydoc
    path("documents-page/<int:pk>/", views.documents_page,name="documents_page"),
    path("documents-page/<slug:str>/", views.documents_page,name="documents_page"),

    path("login-user",views.login_user,name="login_user"),
    path("upload-document",views.upload_document,name="upload_document"),
    # my fun
    path("upload-document/<int:pk>/",views.upload_document,name="upload_document"),

    path('create-advanced-f-company',views.create_advanced_f_company, name="create_advanced_f_company"),
    
    # myfun
    path('create-advanced-f-company/<int:pk>/',views.create_advanced_f_company, name="create_advanced_f_company"),
    path('create-advanced-f-company/<int:pk>/<slug:admindata>/',views.create_advanced_f_company, name="create_advanced_f_company"),
    

    path("advanced-f-company-report",views.advanced_f_company_report,name="advanced_f_company_report"),
    path("f-company-report",views.f_company_report ,name="f_company_report"),

    path("create-f-company-record",views.create_f_company_record,name="create_f_company_record"),
    # my fun
    path("create-f-company-record/<slug:fcom>/<int:pk>/",views.create_f_company_record,name="create_f_company_record"), 
    

    # myfun
    path('delete-doc/<int:id>/', views.delete_doc, name="delete_doc") 
]
