from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from KNB.forms import DepositForm, Withdrawform
from userlogin.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .utils import send_sms
from django.contrib import messages
from KNB.models import Balance

@login_required
def profile(request):
    return render(request, 'content.html')

def home_view(request):
    return render(request, 'index.html')

def auth_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('home-view')
    return render(request, 'login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('login-view')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def logout_request(request):

    logout(request)
    messages.info(request, "You logged out successfully!")
    return redirect('login-view')


def deposit(request):  
    form = DepositForm(request.POST or None)
    pk = request.session.get('pk')
    
    if pk:        
        user = CustomUser.objects.get(pk=pk)
        balance = user.balance
        code_user = f"{user.username}: {user.balance}"
        if not request.POST:
            balance.save()
            print(balance.number)
        if request.method == "POST":
            if form.is_valid():
                num = form.cleaned_data.get('number')
                print(balance.number)
                balance.number = balance.number + num
                print(balance.number)
                balance.save(force_update=True)

        
    return render(request, 'deposit.html')

def withdraw(request):
    
    form = Withdrawform(request.POST or None)
    pk = request.session.get('pk')
    
    if pk:        
        user = CustomUser.objects.get(pk=pk)
        balance = user.balance
        code_user = f"{user.username}: {user.balance}"
        if not request.POST:
            balance.save()
            print(balance.number)
        if request.method == "POST":
            if form.is_valid():
                num = form.cleaned_data.get('number')
                print(balance.number)
                balance.number = balance.number - num
                if balance.number <= 0:
                    return redirect('home-view')
                print(balance.number)
                balance.save(force_update=True)

        
    return render(request, 'withdraw.html')