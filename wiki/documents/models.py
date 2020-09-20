from django.db import models
from django.conf import settings
import json
from django.core.serializers import serialize
from django.db.models.fields import AutoField
from django.db.models.fields import checks



class DocumentQuerySet(models.QuerySet):
    def serialize(self):
        list_values=list(self.values("title","content","author","version"))
        return json.dumps(list_values)

class DocumentManager(models.Manager):
    def get_queryset(self):
        return DocumentQuerySet(self.model,using=self._db)

# Create your models here.
class Document(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    version= models.BigIntegerField(default=1)
    title=models.CharField(max_length=50,blank=True,null=True)
    content=models.TextField(blank=True,null=True)
    modified_timestamp=models.DateTimeField(auto_now=True)
    created_timestamp=models.DateTimeField(auto_now_add=True)

    objects=DocumentManager()

    def __str__(self):
        return self.content or ""


    def serialize(self):
         json_data={
                    'title':self.title,
                    'content':self.content,
                    'version':self.version,
                    'author':self.author.id
                     }

         data=json.dumps(json_data)
         return data
