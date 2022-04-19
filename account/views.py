from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if password:
            if User.objects.filter(username=username).exists():
                print('user taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                print('user created')

        else:
            print('password not match')
        return redirect('login')
    else:
        return render(request, 'account.html')




def login(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']

        user = auth.authenticate(username=username_or_email, password=password)
        if not user:
            auth.authenticate(username=username_or_email, password=password)
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
 
     



