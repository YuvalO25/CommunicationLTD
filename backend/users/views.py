from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin/')  # זמני — נחליף ל-dashboard בהמשך
        else:
            messages.error(request, "Incorrect username or password")
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')
