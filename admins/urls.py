from django.contrib.auth.views import LogoutView
from django.urls import path
from admins import views


urlpatterns = [
  path("admin-login",views.Login.as_view(), name="admin_login"),
  path("logout", LogoutView.as_view(), name="logout"),
  path("admin-main", views.AdminMainView.as_view(), name="admin_main"),
  path("add-user", views.AddUserView.as_view(), name="add-user"),
  path("add-doc", views.AddDocTypeView.as_view(), name="add-doc"),
  path("add-item", views.AddItemView.as_view(), name="add-item"),
  path("add-admin", views.AddAdminView.as_view(), name="add-admin"),
  path("add-comp", views.AddCompanyView.as_view(), name="add-comp"),
  path("add-id", views.AddIdView.as_view(), name="add-id"),
  path("admin-account-report", views.AccountReportView.as_view(), name="admin_account_report"),
  path("admin-documents-report" ,views.DocumentReportView.as_view(), name="admin_documents_report"),
  path("admin-account-report/<int:id>", views.AccountReportView.as_view(), name="delete"),
  path('account/<pk>/delete/',views.AdminDeleteAccount.as_view(),name ='admin_delete_account'),
  path('admin-documents-report/<pk>/delete/',views.AdminDeleteDocument.as_view(),name ='admin_delete_document'),


]