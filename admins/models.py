from django.contrib.auth.models import User
from django.db import models
from datetime import datetime  

# Create your models here.

class new_document(models.Model):
    document = models.CharField(max_length=200)
    def __str__(self):
        return self.document
    

class page_acces(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pages", limit_choices_to={"is_superuser": False})
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="profiles", null=True, limit_choices_to={"is_superuser": True})
    upload = models.BooleanField(default=False)
    documents = models.BooleanField(default=False)
    new_record = models.BooleanField(default=False)
    avanced_record = models.BooleanField(default=False)
    company_report = models.BooleanField(default=False)
    advanced_report = models.BooleanField(default=False)

    

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


