from django.shortcuts import render,redirect
from .forms import login_form,home_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .models import Login
# Create your views here.
def login(request):
    form1 = login_form()
    if request.method == 'POST':
        form1 = login_form(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home')
    return render(request,"login.html",context={'forms':form1})


    # if request.user.is_authenticated:
    #     return redirect('home')  # Redirect if the user is already logged in
    #
    # form1 = login_form()
    # if request.method == 'POST':
    #     form1 = login_form(request.POST)
    #     if form1.is_valid():
    #         ph = form1.cleaned_data['ph']
    #         password = form1.cleaned_data['password']
    #         user = authenticate(request, ph=ph, password=password)
    #         if user is not None:
    #             auth_login(request, user)
    #             return redirect('home')  # Redirect to home after successful login
    #         else:
    #             form1.add_error(None, 'Invalid username or password')
    #
    # return render(request, "login.html", {'forms': form1})
@login_required(login_url='login')
def home(request):
    users = Login.objects.all()

    # phone_number = request.user.ph  # Assuming 'ph' is the phone number field in your user model
    # return render(request, 'home.html',{'phone_number': phone_number})
    return render(request, 'home.html',{'users':users})