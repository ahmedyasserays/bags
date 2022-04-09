from django.contrib import admin
from .models import new_document, ID_name, page_acces, new_item,f_company
# Register your models here.

admin.site.register(new_document)
admin.site.register(ID_name)
admin.site.register(page_acces)
admin.site.register(new_item)
admin.site.register(f_company)


