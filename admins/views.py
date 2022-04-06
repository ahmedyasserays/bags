from types import new_class
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from  .models import ID_name, f_company, login, new_document, new_item, page_acces
# Create your views here.

# admin login page
def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("admin_main")
        else:
            return redirect("admin_login")
        
    return render(request, "admin/admin-login.html")
# admin main page
def admin_main(request):
    if request.method=='POST'and 'newPage' in request.POST:
        # save the page number
        page = request.POST['page']
        page_av = page_acces(page=page)
        page_av.save()
        # save the document number
    # elif request.method=='POST' and 'newDOc' in request.POST:
    elif 'newDoc' in request.POST:
        document = request.POST['document']
        document_i = new_document(document=document)
        document_i.save()
    elif 'newItem' in request.POST:
        # # save the item
        Item = request.POST['Item']
        items= new_item(Item=Item)
        items.save()
       
    elif 'newAdmin' in request.POST:
         # # save the admin
        email = request.POST['email']
        password = request.POST['password']
        item_= login(email=email, password=password)
        item_.save()
        # # add f-company
    elif 'fCompany' in request.POST:
        company= request.POST['company']
        company_f = f_company(company=company)
        company_f.save()
    elif 'newId' in request.POST:
        # # add name and id
        id_key= request.POST['id_key']
        name = request.POST['name']
        id = ID_name(id_key=id_key, name=name)
        id.save()
    return render(request, "admin/admin-main.html")
        
# admin account report
def admin_account_report(request):
    login_admin = login.objects.all()
    context = {'login_admin': login_admin}
    return render(request, "admin/admin-account-m-report.html", context )

def admin_documents_report(request):
    document = login.objects.all()
    context = {'document': document}
    return render(request, "admin/admin-documents-report.html" ,context)

def delete(request,id):
    customer = login.objects.filter(id=id)
    customer.delete()
    return render(request,'admin/admin-account-m-report.html')

