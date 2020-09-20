from django.urls import path,re_path

from .views import DocumentModelListAPIView

urlpatterns = [
    path('',DocumentModelListAPIView.as_view()),#documents/-->list
    ]
#
