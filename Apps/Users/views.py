from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import registerUser
# Create your views here.
def LoginUser(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/projects/curriculum-vitae/')
        else:
            messages.error(request, 'Password or Email is incorrect')
            return redirect('/projects/curriculum-vitae/login')

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/projects/curriculum-vitae/')
        else:
            return render(request, 'Users/login-index.html')




def RegisterUser(request):
    forms = registerUser()
    if request.method == "POST":
        forms = registerUser(request.POST)
        if forms.is_valid():
            user = forms.save()
            # user.is_staff = True
            group = Group.objects.get(name='CurriculumVitae')
            user.groups.add(group)
            # user.save()
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/projects/curriculum-vitae/')

    context = {
        'forms': forms,
    }


    return render(request, 'CurriculumVitae/register-index.html', context)