from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('addList',views.addList,),
    path('addData',views.addData,name='addData'),
    path('viewList',views.viewList,name='viewList'),
    path('index',views.index,name='index'),
]