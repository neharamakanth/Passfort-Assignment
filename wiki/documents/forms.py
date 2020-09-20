from django import forms
from .models import Document
import json
class DocumentForm(forms.ModelForm):
    class Meta():
        model=Document
        fields=['title','content','author','version']


    queryset=None
    def get_queryset(self):
        qs=Document.objects.all()
        self.queryset=qs
        return qs
    def get_object(self,title=None,version=None):
         qs=self.get_queryset().filter(title= title)#qs=self.queryset.filter(id=id)
         if qs.count()>=1:
             return qs.last()
         return None

    def clean(self,*args,**kwargs):
        data=self.cleaned_data
        content=data.get('content',None)
        title=data.get('title',None)
        current_version=data.get('version',None)
        if title is None:
            raise forms.ValidationError("Please give some title to the document!")
        obj=self.get_object(title=title)
        if obj is not None:
            existing_data=json.loads(obj.serialize())
            existing_version=existing_data['version']
            if current_version ==existing_version:
                raise forms.ValidationError("Cannot have same version for the existing title !")
            elif current_version>(existing_version+1):
                raise forms.ValidationError("Cannot skip version for the existing title !")
        else:
            if current_version!=1:
                raise forms.ValidationError("Version of new document should be 1!")
# raising error for empty document
        if content=='':
            content=None
        if content is None:
            raise forms.ValidationError("Please enter some content, cannot create empty document!")
        return super().clean(*args,**kwargs)
