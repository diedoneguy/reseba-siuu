from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(user_name=user_name).exists():
                print('user taken')
            else:
                user = User.objects.create_user(username=user_name,
                                                password=password1)                                
                user.save()
                print('user created')
        else:
            print('password not match')
        return redirect('login')
    else:
        return render(request, 'account.html')
      
def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('wrong logins')
            return redirect('/')
    else:
        return render(request, 'account.html')
def logout(request):
    auth.logout(request)
    return redirect("/")
 
     



