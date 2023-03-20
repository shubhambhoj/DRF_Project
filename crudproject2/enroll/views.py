from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from enroll.forms import Student
from enroll.models import User
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

# ADD AND SHOW DATA 
'''
class AddShow(View):
    def get(self,request):
        fm=Student()
        stud=User.objects.all()
        return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})   
        
    def post(self,request):
        fm=Student(request.POST)
        stud=User.objects.all()
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pwd)
            reg.save()
            fm=Student()
        return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})    
'''    

class AddShow(TemplateView):
    template_name='enroll/addandshow.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        fm=Student()
        stud=User.objects.all()
        context={'form':fm, 'stu':stud}
        return context
    
    def post(self, request):
        fm=Student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pwd)
            reg.save()
        return HttpResponseRedirect('/')
# UPDATE DATA 
'''
class UpdateData(View):
    def get(self,request,id):
        reg=User.objects.get(pk=id)
        fm=Student(instance=reg)
        return render(request, 'enroll/updatestudent.html', {'form':fm})

    def post(self,request,id):
        fm=Student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User(id=id, name=nm, email=em, password=pwd)
            reg.save()
            return HttpResponseRedirect('/')
        return render(request, 'enroll/updatestudent.html', {'form':fm})
'''

class UpdateData(View):
    def get(self,request,id):
        reg=User.objects.get(pk=id)
        fm=Student(instance=reg)
        return render(request, 'enroll/updatestudent.html', {'form':fm})

    def post(self,request,id):
        fm=Student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User(id=id, name=nm, email=em, password=pwd)
            reg.save()
            return HttpResponseRedirect('/')
        return render(request, 'enroll/updatestudent.html', {'form':fm})


# DELETE DATA
'''
class DeleteData(View):
    def post(self,request,id):
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
'''

class DeleteData(RedirectView):
    url='/'
    def get_redirect_url(self,*args, **kwargs):
        print(kwargs)
        pi=User.objects.get(pk=kwargs['id']).delete()
        
        return super().get_redirect_url(*args,**kwargs)
        

############################################################################################
# ADD AND SHOW DATA 
'''
def add_show(request):
    if request.method=='POST':
        fm=Student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pwd)
            reg.save()
            fm=Student()
    else:
        fm=Student()
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})
'''
# UPDATE DATA 
''' 
def update_data(request, id):
    if request.method=='POST':
        fm=Student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User(id=id, name=nm, email=em, password=pwd)
            reg.save()
            return HttpResponseRedirect('/')
    else:
        reg=User.objects.get(pk=id)
        fm=Student(instance=reg)
        
    return render(request, 'enroll/updatestudent.html', {'form':fm})
'''
# DELETE DATA
'''
def delete_data(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
'''





