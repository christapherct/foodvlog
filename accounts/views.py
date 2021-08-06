from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')
        user = auth.authenticate(username=username, password=password)
        print("user printed")

        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/')
            else:
                return redirect('/')
        else:
            messages.info(request,"Invalid input")
            return redirect('login')
    else:
        return render(request,"login.html")

def register(request):
    if request.method == "POST":
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Mail Id already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
        else:
            return redirect('register')
        return redirect('/')
    else:

        return render(request, 'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

