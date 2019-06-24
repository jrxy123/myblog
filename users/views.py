from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages, auth
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# Create your views here.

def checkuser(username):
    try:
        user = CustomUser.objects.get(username=username)
        if user is not None:
            return True
    except:
        return False

# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm()
#         if checkuser(request.POST['username']):
#             messages.error('Already existing username.')
#             return render(request, 'users/signup.html')
#         if form.is_valid():
#             user = CustomUser.objects.create_user(username=request.POST['username'], password=request.POST['password'])
#             auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return redirect('home')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'users/signup.html', {'form': form})

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error('Incorrect username or password')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
