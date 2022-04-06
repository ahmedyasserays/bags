from xml.dom.minidom import Document
from django.db import models
from datetime import datetime  

# Create your models here.

class new_document(models.Model):
    document = models.CharField(max_length=200)
    def __str__(self):
        return self.document
    
class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    last_login = models.DateField(default=datetime.now(), blank=True)
    document = models.ForeignKey(new_document, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.email
    
    
class page_acces(models.Model):
    page = models.CharField(max_length=200)
    def __str__(self):
        return self.page
    

class new_item(models.Model):
    Item = models.CharField(max_length=200)
    def __str__(self):
        return self.Item
    
class f_company(models.Model):
    company = models.CharField(max_length=200)
    def __str__(self):
        return self.company
    
class ID_name(models.Model):
    id_key = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name