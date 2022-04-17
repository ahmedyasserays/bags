from django.urls import path
from . import views


urlpatterns = [
    path('advance_f_company/',views.AdvancedFcompanyView.as_view(),name='advancedFcompanyapi')

]