from django.shortcuts import render,redirect
from studentapp.models import student

class SMSHomeView:

    def GET(self,request):
        return render(request,'studentapp/home.html')
    