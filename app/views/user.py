from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        #Django have a own form for authentication users.
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect ('tasks')
    else:   
        form = UserCreationForm()

    return render(request,'users/form_user.html', {'form':form} )


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect ('tasks')
        else:
            messages.error(request, 'Wrong input data.')
            return redirect('login')
    form = AuthenticationForm()
    return render (request,'users/login.html',{'form':form})
    
def logout_user(request):
    logout(request)
    return redirect ('login')