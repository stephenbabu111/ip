from django.shortcuts import render
from .models import login_table,ip_table

def home_view(request):


    ip=(request.META.get('REMOTE_ADDR'))
    iptable=ip_table()
    iptable.ip=ip
    iptable.save()
    return render(request, 'loginapp/home.html')

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
        var1=login_table.objects.filter(username=username)
        var2=login_table.objects.filter(password=password)
        if not var1 and not var2:
            print('regestration sucessfull')
            ltable.username=username
            ltable.password=password
            ltable.name=name
            ltable.email=email
            ltable.phone=phone
            ltable.save()
            str1='loginapp/signupconf.html'

        else:
            print('regestration failed')
            str1='loginapp/signupfail.html'

        return render(request,str1)

def login_view(request):
    return render(request,'loginapp/login.html')
def conf_login_view(request):
    if request.method=='POST':
        print('login conf view is running')
        username=request.POST.get('username')
        password=request.POST.get('password')
        log=login_table.objects.filter(username=username,password=password).values('password','name')
        print(log)
        str='loginapp/loginconf.html'
        str1=' '
        name=' '
        if not log:
            str1='username does not exist'
            str='loginapp/loginfail.html'

        else:
            print('login was succesfull')

        log_dict={'str1':str1,'name':username}
    return render(request,str,log_dict)


