from typing import Type
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from book import models
import book
from book.models import Equation,Note,TimeTable
from book.forms import EquationForm, NoteForm,RegistrationForm,TimeTableForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='book:login')
def index(request):
    subject=Note.objects.filter(user=request.user).values('subject').distinct()
    context={'subject':subject}
    return render(request,'book/index.html',context)
@login_required(login_url='book:login')
def module(request,data):
    try:
        global sd
        sd=data
        module=Note.objects.filter(user=request.user,subject=sd).values('module').distinct()
        context={'module':module}
        return render(request,'book/module.html',context)
    except NameError:
        return redirect('book:index')
@login_required(login_url='book:login')
def heading(request,data):
    try:
        global md
        md=data
        # head=Note.objects.get(user=request.user,module=md,subject=sd)
        heading=Note.objects.filter(user=request.user,module=md,subject=sd).values('heading').distinct()
        context={'heading':heading}
        return render(request,'book/heading.html',context)
        
    except NameError:
        return redirect('book:index')
@login_required(login_url='book:login')
def content(request,data):
    try:
        global hd
        hd=data
        id=Note.objects.get(user=request.user,module=md,subject=sd,heading=hd)
        content=Note.objects.filter(user=request.user,module=md,subject=sd,heading=hd)
        context={'content':content,'head':hd,'id':id}
        return render(request,'book/content.html',context)
    except NameError:
        return redirect('book:index')
@login_required(login_url='book:login')
def addnote(request):
    if request.method=="POST":
        note=Note()
        subject=request.POST['subject']
        module=request.POST['module']
        heading=request.POST['heading']
        content=request.POST['content']
        note.user=request.user
        note.subject=subject
        note.module=module
        note.heading=heading
        note.content=content
        note.save()
        return redirect('book:index')
    form=NoteForm()
    context={'form':form}
    return render(request,'book/addnote.html',context)
@login_required(login_url='book:login')
def subject_equation(request):
    subject=Equation.objects.filter(user=request.user).values('subject').distinct()
    context={'subject':subject}
    return render(request,'book/sub_equa.html',context)
@login_required(login_url='book:login')
def module_equation(request,data):
    try:
        global esd
        esd=data
        module=Equation.objects.filter(user=request.user,subject=esd).values('module').distinct()
        context={'module':module}
        return render(request,'book/mod_equa.html',context)
    except NameError:
        return redirect('book:subject_equation')
@login_required(login_url='book:login')
def heading_equation(request,data):
    try:
        global emd
        emd=data
        heading=Equation.objects.filter(user=request.user,subject=esd,module=emd).values('heading').distinct()
        context={'heading':heading}
        return render(request,'book/head_equa.html',context)
    except NameError:
        return redirect('book:subject_equation')
@login_required(login_url='book:login')
def equation(request,data):
    try:
        global ehd
        ehd=data
        content=Equation.objects.filter(user=request.user,module=emd,subject=esd,heading=ehd)
        context={'content':content}
        return render(request,'book/equation.html',context)
    except NameError:
        return redirect('book:subject_equation')
@login_required(login_url='book:login')
def addequation(request):
    if request.method=="POST":
        equation=Equation()
        subject=request.POST['subject']
        module=request.POST['module']
        heading=request.POST['heading']
        equa=request.POST['equation']
        equation.user=request.user
        equation.subject=subject
        equation.module=module
        equation.heading=heading
        equation.equation=equa
        equation.save()
        return redirect('book:subject_equation')
    form=EquationForm()
    context={'form':form}
    return render(request,'book/addequation.html',context)

def registerPage(request):
    if request.method=="POST":
        print("sabarinath")
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:index')
    form=RegistrationForm()
    context={'form':form}
    return render(request,'book/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('book:index')
    else:
        
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('book:index')
            else:
                messages.info(request,'Username OR Password is Incorrect')
                context={}
                return render(request,'book/login.html',context)
      
    return render(request,'book/login.html')
def logoutPage(request):
    logout(request)
    return redirect('book:login')
def addtimetable(request):
    if request.method=="POST":
        timetable=request.POST['timetable']
        time=TimeTable()
        time.user=request.user
        time.timetable=timetable
        time.save()
        return redirect('book:displaytimetable')

    form=TimeTableForm()
    context={'form':form}
    return render(request,'book/addtimetable.html',context)
def displaytimetable(request):
    timetable=TimeTable.objects.filter(user=request.user)
    context={'timetable':timetable}
    return render(request,'book/displaytimetable.html',context)


def edit_timetable(request):
    if request.method=="POST":
        timetable=TimeTable.objects.get(user=request.user)
        form=TimeTableForm(request.POST,instance=timetable)
        if form.is_valid():
            form.save()
            return redirect('book:displaytimetable')
    timetable=TimeTable.objects.get(user=request.user)
    form=TimeTableForm(instance=timetable)
   
    context={'form':form}
    return render(request,'book/edittimetable.html',context)
def edit_note(request,id):
    if request.method=="POST":
        note=Note.objects.get(pk=id)
        form=NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('book:content',data=hd)
    note=Note.objects.get(pk=id)
    form=NoteForm(instance=note)
    context={'form':form,'note':note}
    return render(request,'book/edit_note.html',context)

def delete_note(request,id):
    note=Note.objects.get(pk=id)
    note.delete()
    return redirect('book:index')




