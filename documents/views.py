# from locale import NOEXPR
from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
from .models import advanceFcompany, newFCompany, uplaodingDocument
from admins.models import new_document, new_item, f_company

from django.http import JsonResponse
import json
from .serializer import advanceFcompanySerializer,uploadingDocumentSerializer,newFCompanySerializer
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from admins.serializer import idnameSerializer
from admins.models import ID_name
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request, "index.html")
# advanced-f-company-report
def advanced_f_company_report(request):
    advance = advanceFcompany.objects.all()
    openbal=0
    for item in advance:
        openbal=openbal+(item.NetAmount)
        item.balance=openbal
    # pagination
    page = request.GET.get('page', 1)

    paginator = Paginator(advance, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {"users":users}
    return render(request, "user/advanced-f-company-report.html", context)
# document page for the user
def documents_page(request, pk=None, str=None):
    if pk is not None:
        obj=uplaodingDocument.objects.get(pk=pk)
        obj.delete()
        return redirect('/documents-page')

    if str=="sharedoc":
        document_show = uplaodingDocument.objects.all()
        context = {"document_show":document_show, "sharedoc":True}
        return render(request, "user/documents-page.html",context)
    
    document_show = uplaodingDocument.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(document_show, 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {"users":users}
    return render(request, "user/documents-page.html",context)
# login the user
def login_user(request):
    return render(request,"user/login.html")

# upload documnets of the user
from django.core.files.storage import FileSystemStorage
def upload_document(request, pk=None):
    if (pk is not None) :
        try:
            data=uplaodingDocument.objects.get(documentNumber=pk)
            
            if data is not None:
                serializer = uploadingDocumentSerializer(data)
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse({"1"})
        except Exception as e:
            print("exception is :", e)
            return JsonResponse("0", safe=False)

    type = new_document.objects.all()
    item = new_item.objects.all()
    context= {'item':item, 'type':type}
    # post request to save the data
    if request.method =="POST" and 'file' in request.FILES: 
        documentNumber = request.POST['documentNumber']
        itemType = request.POST['itemType']
        documentDate = request.POST['documentDate']        
        DocumentType = request.POST['DocumentType']
        File = request.FILES['file'] 
        fs = FileSystemStorage()
        filename = fs.save(File.name, File)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        if documentNumber == "": # for dcoument number = none
            documentNumber =None
        upload = uplaodingDocument(documentNumber=documentNumber, 
                                 itemType=itemType, documentDate=documentDate, DocumentType=DocumentType,file=File)
        upload.save()

    return render(request, "user/upload-document.html", context)

# create f-company recods
@api_view(['GET','POST'])
def create_advanced_f_company(request, pk=None, admindata=None):
    if (pk is not None) and (admindata=="fromadmin"):
        print("Creating advanced")
        try:
            obj=ID_name.objects.get(id_key=pk)
            serializer = idnameSerializer(obj)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse("0", safe=False)

    if pk is not None:
        try:
            data=advanceFcompany.objects.get(idComapny=pk)
            if data is not None:
                serializer = advanceFcompanySerializer(data)
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse({"1"})
        except Exception as e:
            print("exception is :", e)
            return JsonResponse("0", safe=False)

    
    if request.method=="POST":
        date = request.POST['date']
        idComapny= request.POST['idComapny']
        name = request.POST['name']
        recevingNumber = request.POST['recevingNumber']
        receivingAmount = request.POST['receivingAmount']
        expenceNumber = request.POST['expenceNumber']
        expenceAmount = request.POST['expenceAmount']
        depositeAmount = request.POST["depositeAmount"]
        paymentAmount = request.POST["paymentAmount"]
        DepPayDate = request.POST["DepPayDate"]
        FCompany = request.POST["FCompany"]
        RecLink = request.POST["RecLink"]
        receiDepPay = request.POST["receiDepPay"]
        NetAmount = request.POST["NetAmount"]
        details = request.POST["details"]
        notes = request.POST["notes"]
        if recevingNumber == "": # for the null of receving number
            recevingNumber = None
        if receivingAmount == "":
            receivingAmount =None # for the reciving amount
        if expenceNumber == "": # for the expence amount
            expenceNumber =None 
        if expenceAmount == "": # for the expense amount
            expenceAmount =None
        if depositeAmount == "": # for the deposite amount
            depositeAmount =None
        if paymentAmount == "": # for the payment amount
            paymentAmount = None
        if receiDepPay == "": # for the receiDepPay amount
            receiDepPay = None
        if NetAmount == "" or "Nan":
            NetAmount = 0

        try:
            obj=advanceFcompany.objects.get(idComapny=idComapny)
            print("user already exits with this id")
            messages.info(request, "User already exits with this user id enter another id")
        except Exception as e:
            print("exception is :", e)
            print("save the record")
            advance = advanceFcompany(date=date, idComapny=idComapny,name=name,recevingNumber=recevingNumber, receivingAmount=receivingAmount,expenceAmount=expenceAmount,
            expenceNumber=expenceNumber, depositeAmount=depositeAmount, paymentAmount=paymentAmount,DepPayDate=DepPayDate, FCompany=FCompany,receiDepPay=receiDepPay,details=details,notes=notes,NetAmount=NetAmount,RecLink=RecLink)
            advance.save()

    return render(request,"user/create-advanced-f-company-record.html")

def create_f_company_record(request, fcom=None, pk=None):
    if (fcom is not None) and (pk is not None):
        try:
            data=newFCompany.objects.get(FCompany=fcom, depostieAmount=pk)
            if data is not None:
                serializer = newFCompanySerializer(data)
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse({"1"})
        except Exception as e:
            print("exception is :", e)
            return JsonResponse("0", safe=False)
    type = f_company.objects.all()
    item = new_item.objects.all()
    context= {'item':item, 'type':type}
    # netAmount = depostieAmount-paymenetAmount
    if request.method =="POST":
        date = request.POST['date']
        FCompany = request.POST['FCompany']
        depostieAmount= request.POST['depostieAmount']
        paymenetAmount = request.POST['paymenetAmount']
        DepPAyDate = request.POST['DepPAyDate']
        netAmount = request.POST['netAmount']
        if paymenetAmount == "": # conditions for the payment amount
            paymenetAmount = None
        if netAmount == "" or "NaN": # condtions for the netAmout
            netAmount = 0
        if depostieAmount == "": # condtions for the deposite amount
            depostieAmount = None
        fcompany = newFCompany(date=date,FCompany=FCompany,depostieAmount=depostieAmount,paymenetAmount=paymenetAmount,
                               DepPAyDate=DepPAyDate,netAmount=netAmount)
        fcompany.save()
    return render(request,"user/create-f-company-record.html", context)

def f_company_report(request):
    company = newFCompany.objects.all()
    openbal=0
    for item in company:
        openbal=openbal+(item.netAmount)
        item.balance=openbal
    page = request.GET.get('page', 1)

    paginator = Paginator(company, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    
    context = {"users":users,"sharedoc":True}
   
    return render(request,"user/f-company-report.html",context)

def delete_doc(request, id):
    print("id is :", id)
    pass