from django.shortcuts import render,redirect
from studentapp.models import student
import datetime

# Create your views here.
def home_view(request):
    return render(request,'studentapp/home.html')

def insert_student_view(request):
    if request .method =="POST":
        
        r = request.POST.get('rn')
        n = request.POST.get('nm')
        m = request.POST.get('mk')
        s1 = student (roll=r,name=n,marks=m)
        s1.save()
        # if s1:
        #     context = {'msg':'Student inserted successfully'}
        # else:
        #     context = {'msg':'Failed to insert student'}
            
        # return render(request,'studentapp/insert.html',context)
    
    return render(request,'studentapp/insert.html')


def display_all_view(request):

    student_db= student.objects.all()
    
    context ={"data":student_db}

    return render(request,'studentapp/display.html',context )

def update_student_view(request,roll):
    
    s1 = student.objects.get(roll=roll)

    if request.method == "POST":

        updated_n = request.POST.get('nm')
        updated_m = request.POST.get('mk')

        s1.name = updated_n
        s1.marks = updated_m
        s1.save()
        return redirect("/display-all/")

    return render(request,'studentapp/update.html',{'data':s1})

def delete_student_view(request,roll):
    
    s1 = student.objects.get(roll=roll)

    if request.method == 'POST':
        s1.delete()
        return redirect("studentapp/display-all/")

    return render(request,'studentapp/delete.html',{'data':s1})

 