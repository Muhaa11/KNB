from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from KNB.forms import DepositForm, Withdrawform
from userlogin.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from KNB.models import Balance




def home_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        if request.POST.get('submit') == 'signIn':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['pk'] = user.pk
                return redirect('home-view')

        elif request.POST.get('submit') == 'signUp':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.save()
                return redirect('home-view')
            else:
                form = SignUpForm()
    return render(request, 'index.html', {'form': form})    

@login_required
def balance(request):
    return render(request, 'balance.html')





def logout_request(request):

    logout(request)
    return redirect('home-view')

@login_required
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

@login_required
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
                if balance.number < 0:
                    messages.info(request, "Insufficient funds!")
                    return redirect('withdraw.html')
                print(balance.number)
                balance.save(force_update=True)

        
    return render(request, 'withdraw.html')