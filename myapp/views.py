from django.shortcuts import render,redirect
from .forms import formz,formz2,formz3
import random
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .models import Login,Home,Registration
import logging
logger = logging.getLogger(__name__)
# Create your views here.
def login(request):
    form1 = formz()
    if request.method == 'POST':
        form1 = formz(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home_page')
    return render(request, "login.html", context={'form': form1})


#     form1 = formz()
#     if request.method == 'POST':
#         form1 = formz(request.POST)
#         if form1.is_valid():
#             username = form1.cleaned_data.get('username')
#             password = form1.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 logger.debug(f"User {username} authenticated successfully.")
#                 return redirect('home_page')
#             else:
#                 # Return an 'invalid login' error message.
#                 logger.debug(f"User {username} failed to authenticate.")
#                 return render(request, "login.html", context={'form': form1, 'error': 'Invalid credentials'})
#     return render(request, "login.html", context={'form': form1})
def registration(request):
    form2 = formz2()
    if request.method == 'POST':
        form2 = formz2(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect("login")
    return render(request,"register.html",context={'form': form2})
@login_required(login_url='login')
def home_page(request):
    # users = Login.objects.all()
    # user = request.user
    # username = user.username
    # return render(request, 'home.html',{'users':users, 'username': username})
    form3 = formz3()
    user = request.user
    username = user.username
    count = Login.objects.filter(username=username).count()
    si_number = min(count + 1, 8192)
    member_id = random.randint(1000, 9999)
    left_customer = random.randint(0, 20)
    right_customer = random.randint(0, 20)
    amount = (left_customer + right_customer) * 25
    rebirth = (count + 1) % 50 == 0 or (count + 1) % 100 == 0
    if rebirth:
        random_suffix = str(random.randint(1000, 9999)).zfill(4)
        new_member_id = f'RL{username[-7:]}{random_suffix}'
        member_id = new_member_id

    if request.method == 'POST':
        form3 = formz3(request.POST)
        if form3.is_valid():
            home_instance = form3.save(commit=False)
            home_instance.count = count
            home_instance.username = user
            home_instance.si_number = si_number
            home_instance.member_id = member_id
            home_instance.left_customer = left_customer
            home_instance.right_customer = right_customer
            home_instance.amount = amount
            home_instance.rebirth = rebirth
            home_instance.save()
            return redirect('home_page')
        # else:
        #     form3 = formz3()


    users = Home.objects.all()
    # users = Home.objects.filter(user=user)
    return render(request, 'home.html',
                          {'form': form3,
                           'users': users,
                           'username': username,
                           'count': count,
                           'si_number': si_number,
                           'member_id': member_id,
                           'left_customer': left_customer,
                           'right_customer': right_customer,
                           'amount': amount,
                           'rebirth': rebirth})