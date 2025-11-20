from django.shortcuts import render, redirect
from studentapp.models import Student

# Create your views here.
def home_view(request):
    return render(request, 'studentapp/home.html')

def insert_view(request):

    if request.method == 'POST':
        r = request.POST.get('roll')
        n = request.POST.get('name')
        m = request.POST.get('marks')

        s1 = Student(roll=r, name=n, marks=m)
        s1.save()
        return redirect('display')
        
        # return render(request,'studentapp/insert.html',)
    return render(request, 'studentapp/insert.html')

def display_view(request):
    student_db = Student.objects.all()

    context  = {'data': student_db}

    return render(request, 'studentapp/display.html', context)

def update_view(request, id):

    s1 = Student.objects.get(roll=id)

    if request.method == 'POST':
        n = request.POST.get('name')
        m = request.POST.get('marks')

        s1.name = n
        s1.marks = m
        s1.save()
        return redirect('display')

    context = {'data': s1}
    return render(request, 'studentapp/update.html', context)

def delete_view(request, id):
    s1 = Student.objects.get(roll=id)
    if request.method == 'POST':
        s1.delete()
        return redirect('display, HELLO WORLD')
    return render(request, 'studentapp/delete.html', {'data': s1})
