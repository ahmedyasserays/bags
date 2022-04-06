from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from admins import  views
urlpatterns = [
  path("admin-login",views.admin_login, name="admin_login"),
  path("admin-main",views.admin_main, name="admin_main"),
  path("admin-account-report", views.admin_account_report, name="admin_account_report"),
  path("admin-documents-report" ,views.admin_documents_report, name="admin_documents_report"),
  path("admin-account-report/<int:id>", views.delete, name="delete")
]