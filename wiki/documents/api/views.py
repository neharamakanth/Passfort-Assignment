from documents.models import Document as DocumentModel
from django.views.generic import View
from django.http import HttpResponse
from .utils import is_json
from .mixins import CSRFExemptMixin
from wiki.mixins import HttpResponseMixin
import json
from documents.forms import DocumentForm

#'documents/' endpoint for both detail and list view of CRUD operations
#its always better to have single end point for all crud operations

class DocumentModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    '''list view for create and retrieve '''

    is_json=True
    queryset=None
    def get_queryset(self):
        qs=DocumentModel.objects.all()
        self.queryset=qs
        return qs

    def get_object(self,title=None,version=None):
         if title is None:
             return None
         qs=self.get_queryset().filter(title= title)
         if qs.count()>=1:
             if version:
                 return qs.last()
             return qs
         return None

    def get(self,request,*args,**kwargs):
        passed_data=json.loads(request.body)
        passed_title=passed_data.get("title",None)
        latest_flag=passed_data.get("latest",None)
        if passed_title :
            obj=self.get_object(title=passed_title,version=latest_flag)
            if obj is None:
                data=json.dumps({'message':'No document found for this title'})
                return self.render_to_response(data,status=404)
            json_data=obj.serialize()
            return self.render_to_response(json_data)
        else:
            qs=self.get_queryset()
            if qs.count()<1:
                data=json.dumps({'message':'No documents available'})
                return self.render_to_response(data,status=404)
            json_data=qs.serialize()
            return self.render_to_response(json_data)

    def post(self,request,*args,**kwargs):
        print(request.POST)
        is_valid=is_json(request.body)
        if not is_valid :
            err_data=json.dumps({'message':'Invalid data,please send the data in Json format'})
            return self.render_to_response(err_data,status=400)
        passed_data=json.loads(request.body)
        passed_title=passed_data.get("title")
        obj=self.get_object(title=passed_title,version=True)
        if obj is None:
            passed_data['version']=1
            form=DocumentForm(passed_data)
            if form.is_valid():
                obj=form.save(commit=True)
                obj_data=obj.serialize()
                return self.render_to_response(obj_data,status=201)
            if form.errors:
                data=json.dumps(form.errors)
                return self.render_to_response(data,status=400)
        old_data=json.loads(obj.serialize())
        old_version=old_data['version']
        new_data=passed_data
        new_data['version']=old_version+1
        print(' existing version of document',old_data)
        print('new version of document',new_data)
        form=DocumentForm(new_data)
        if form.is_valid():
            obj=form.save(commit=True)
            obj_data=obj.serialize()
            print(obj_data)
            return self.render_to_response(obj_data,status=201)
        if form.errors:
            data=json.dumps(form.errors)
            return self.render_to_response(data,status=400)











    def put(self,request,*args,**kwargs):
        print(request.body)
        # print(dir(request))
        # print(request.POST)-->not present in put request ,access using body
        # print(request.data)
        is_valid=is_json(request.body)
        if not is_valid :
            err_data=json.dumps({'message':'Invalid data,please send the data in Json format'})
            return self.render_to_response(err_data,status=400)
        passed_data=json.loads(request.body)
        passed_title=passed_data.get("title",None)
        if passed_title is None:
            err_data=json.dumps({'title':'this field is required to update an item'})
            return self.render_to_response(err_data,status=400)
        obj=self.get_object(title=passed_title)
        if obj is None:
            data=json.dumps({'message':'object is not found'})
            return self.render_to_response(data,status=404)
        old_data=json.loads(obj.serialize())
        print('old data',old_data)
        print('new data for update',passed_data)
        for key,value in passed_data.items():
            old_data[key]=value
        modified_data=old_data
        form=DocumentForm(modified_data,instance=obj)
        if form.is_valid():
            obj=form.save(commit=True)
            obj_data=json.dumps(modified_data)
            return self.render_to_response(obj_data,status=200)

        if form.errors:
            data=json.dumps(form.errors)
            return self.render_to_response(data,status=400)

        json_data=json.dumps({'message':'something is updated'})
        return self.render_to_response(json_data)

    def delete(self,request,*args,**kwargs):
        is_valid=is_json(request.body)
        if not is_valid :
            err_data=json.dumps({'message':'Invalid data,please send the data in Json format'})
            return self.render_to_response(err_data,status=400)
        passed_data=json.loads(request.body)
        passed_title=passed_data.get("title",None)
        print(passed_title)
        if passed_title is None:
            err_data=json.dumps({'title':'this field is required to delete an item'})
            return self.render_to_response(err_data,status=400)
        obj=self.get_object(title=passed_title)
        if obj is None:
            data=json.dumps({'message':'object is not found'})
            return self.render_to_response(data,status=404)
        deleted_,item_deleted=obj.delete()
        print('deleted item is ' ,item_deleted)
        if deleted_==1:
            json_data=json.dumps({'message':'object is deleted'})
            return self.render_to_response(json_data,status=200)
        json_data=json.dumps({'message':'cannot delete the item,try later'})
        return render_to_response(json_data,status=400)
