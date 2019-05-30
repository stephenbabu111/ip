from django.shortcuts import render
from .models import login_table

def home_view(request):
    return render(request,'loginapp/home.html')
def signup_view(request):
    return render(request,'loginapp/signup.html')
def conf_signup_view(request):
    if request.method=="POST":
        print('this view is running')
        username=request.POST.get('username')
        password=request.POST.get('password')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')



        var=0




        ltable=login_table()
        var=login_table.objects.filter(id=1)
        print(var)
        if username!=username:
            str1='loginapp/home.html'


        else:
            ltable.username=username
            ltable.password=password
            ltable.name=name
            ltable.email=email
            ltable.phone=phone
            ltable.save()
            str1='loginapp/signupconf.html'

        return render(request,str1)

def login_view(request):
    return render(request,'loginapp/login.html')
