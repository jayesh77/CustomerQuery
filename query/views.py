from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import queryform, EditForm
from . models import  querydata,customerdata

def querypage(request):
    fm=queryform()
    if request.POST :
        fm = queryform(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse("Query sbmited sucessfully")
    return render(request,'query/querypage.html',{'form':fm})

def follow_up(request):
        if request.user.is_staff:
            querys=querydata.objects.all()
            ob=customerdata.objects.all
            return render(request,'query/follow_up.html',{'ob':ob,'querys':querys})
        else:
            return HttpResponseRedirect('/login/')



def log(request):
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                print('gopal')
                uname=fm.cleaned_data['username']
                pas=fm.cleaned_data['password']
                us=authenticate(username=uname,password=pas)
                if us is not None:
                    print('gopal22')
                    login(request,us)
                    return HttpResponseRedirect('/follow_up/')
        else:
            fm=AuthenticationForm()
        return render(request,'query/login.html',{'form':fm})


def out(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def updatequery(request,id):
    if request.user.is_staff:
        if request.method == "POST":
            pi = querydata.objects.get(pk=id)
            form = EditForm(request.POST, instance=pi)
            if form.is_valid():
                cs=form.cleaned_data['add_to_customer_list']
                if cs:
                    name=form.cleaned_data['name']
                    s=customerdata(customer=name)
                    s.save()
                form.save()
            return HttpResponseRedirect('/follow_up')
        else:
                pi = querydata.objects.get(pk=id)
                form = EditForm(instance=pi)
        return render(request, 'query/updatequery.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

def deletequery(request,id):
    if request.user.is_staff:
        if request.method == "POST":
            pi = querydata.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/follow_up')
