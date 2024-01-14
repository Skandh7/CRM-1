from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# def add_show(request):
#     stud = User.objects.all()
#     if request.method == 'POST':
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             nm = fm.cleaned_data['name']
#             em = fm.cleaned_data['email']
#             pw = fm.cleaned_data['password']
#             reg = User(name=nm, email=em, password=pw)
#             reg.save() 
#             fm = StudentRegistration()
#     else:
#         fm = StudentRegistration()
#         stud = User.objects.all()

#     return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})
# add_show function
def add_show(request):
    stud = User.objects.all()

    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return redirect('addandshow')  # Redirect to the same view after form submission
    else:
        fm = StudentRegistration()

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

#This function will delete data 
def delete_data(request,id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
#This function will update data 
def update_data(request,id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})
