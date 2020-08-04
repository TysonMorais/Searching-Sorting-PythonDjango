from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas

# Create your views here.
def index(request):
    return render(request,'index.html')

def addList(request):
    return render(request,'addList.html')

def addData(request):
    user_name = request.POST['user_name']
    guardian_name = request.POST['guardian_name']
    house_no = request.POST['house_no']
    house_name = request.POST['house_name']
    gender = request.POST['gender']
    age = request.POST['age']
    id_card_no = request.POST['id_card_no']
    booth_no = request.POST['booth_no']

    datas = Datas(user_name=user_name,guardian_name=guardian_name,house_no=house_no,house_name=house_name,gender=gender,age=age,id_card_no=id_card_no,booth_no=booth_no)
    datas.save()

    return render(request,'addList.html')

def viewList(request):
    all_data = Datas.objects.all()
    return render(request,'viewList.html',{'alldata':all_data})