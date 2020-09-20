from django.contrib import admin
from .forms import DocumentForm
from .models import Document

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display=["title","content",'version',"author","modified_timestamp","created_timestamp"]
    list_filter=['title']
    form=DocumentForm
    # class Meta():
    #     model=Status

# Register your models here.
admin.site.register(Document,DocumentAdmin)
