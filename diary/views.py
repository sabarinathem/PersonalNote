from django.db.models.fields import DateField, DateTimeField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from diary.models import Diary
from diary.form import DiaryForm
import datetime

from django.contrib.auth.decorators import login_required

@login_required(login_url='book:login')

def index(request):
    diary=Diary.objects.order_by('-id')
    context={'diary':diary}
    return render(request,'diary/index.html',context)
@login_required(login_url='book:login')
def add(request):
    if request.method=='POST':
        diary=Diary()
        diary.user=request.user
        diary.text=request.POST['text'] 
        diary.save()
        return redirect('diary:index') 
    else:
        df=DiaryForm()
    context={'form':df}
    return render(request,'diary/add.html',context)
@login_required(login_url='book:login')
def main(request):
    return render(request,'diary/main.html')
@login_required(login_url='book:login')
def diary(request,id):
    diary=Diary.objects.get(pk=id)
    context={'diary':diary}
    return render(request,'diary/diary.html',context)
@login_required(login_url='book:login')
def edit(request,id):
    if request.method=="POST":
        text=request.POST['text']
        diary=Diary.objects.get(pk=id)
        diary.text=text
        diary.date=datetime.datetime.now()
        # d=datetime.datetime.now()
        # diary.date.Date=d.date()
        # diary.date.Time=d.strftime("%I:%M:%S")

        diary.save()
        return redirect('diary:index')
  
    diary=Diary.objects.get(pk=id)
    form=DiaryForm(instance=diary)
   
    context={'form':form,'id':id}
    return render(request,'diary/edit.html',context)
    
@login_required(login_url='book:login')
def delete(request,id):
    diary=Diary.objects.get(pk=id)
    diary.delete()
    return redirect('diary:index')

