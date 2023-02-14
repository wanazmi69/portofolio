from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponse


from django.views.generic.detail import DetailView

from .forms import registerUser, PersonaDataForm_set, BacgroundSchoolForm_set, WorkHistoryForm_set, LicenceOrQualificationForm_set, LanguageSkillForm_set


from .models import PersonalData, BacgroundSchool, WorkHistory, LicenceOrQualification, LanguageSkill
# Create your views here.

def index(request):
    if request.user.is_authenticated:

        dataUsers = PersonalData.objects.all().filter(email=request.user.email)

        print(dataUsers)
        context = {
            'dataUsers': dataUsers,
        }


        return render(request, 'CurriculumVitae/index.html', context)

    return render(request, 'CurriculumVitae/index.html')

@login_required(login_url='/projects/curriculum-vitae/login')

def mycv(request):

    Users = User.objects.filter(id=request.user.id)
    
    for x in Users:
        print(x.id)


    context = {

        'Users': Users,
    }
    return render(request, 'CurriculumVitae/mycv-index.html', context)
def shareLinkCV(request, id):
    User= User.objects.get(id=id)



    context = {
        'User': User,
    }
    return render(request, 'CurriculumVitae/mycv-index.html', context)




@login_required(login_url='/projects/curriculum-vitae/login')
def createCV(request):


        
    formPersonalDataUser = PersonaDataForm_set(instance=request.user)
    formBacgroundSchoolUser = BacgroundSchoolForm_set(instance=request.user)
    formWorkHistoryUser = WorkHistoryForm_set(instance=request.user)
    formLicenceOrQualificationUser = LicenceOrQualificationForm_set(instance=request.user)
    formLanguageSkillUser = LanguageSkillForm_set(instance=request.user)

    if request.method == 'POST':
        formPersonalData = PersonaDataForm_set(request.POST or None, request.FILES or None, instance=request.user)
        formBacgroundSchool = BacgroundSchoolForm_set(request.POST or None, instance=request.user)
        formWorkHistory = WorkHistoryForm_set(request.POST or None, instance=request.user)
        formLicenceOrQualification = LicenceOrQualificationForm_set(request.POST or None, instance=request.user)
        formLanguageSkill = LanguageSkillForm_set(request.POST or None, instance=request.user)
        if formPersonalData.is_valid() and formBacgroundSchool.is_valid() and formWorkHistory.is_valid() and formLicenceOrQualification.is_valid() and formLanguageSkill.is_valid():
            formPersonalData.save()
            formBacgroundSchool.save()
            formWorkHistory.save()
            formLicenceOrQualification.save()
            formLanguageSkill.save()
            return redirect('/projects/curriculum-vitae/mycv')




    context = {
        'formPersonalData':formPersonalDataUser,
        'formBacgroundSchool':formBacgroundSchoolUser,
        'formWorkHistory':formWorkHistoryUser,
        'formLicenceOrQualification':formLicenceOrQualificationUser,
        'formLanguageSkill':formLanguageSkillUser,
      
    }
    return render(request, 'CurriculumVitae/create-cv-index.html', context)

@login_required(login_url='/projects/curriculum-vitae/login')
def exportPDF(request):
    
    Users = User.objects.filter(id = request.user.id)
    context = {
        'Users': Users,
    }
    return render(request, 'CurriculumVitae/pdf-output.html', context)






def LoginUser(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/projects/curriculum-vitae/mycv')
        else:
            messages.error(request, 'Password or Email is incorrect')
            return redirect('/projects/curriculum-vitae/login')

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/projects/curriculum-vitae/mycv')
        else:
            return render(request, 'CurriculumVitae/login-index.html')




def RegisterUser(request):
    forms = registerUser()
    modelDataUser = [
        BacgroundSchool,
        WorkHistory,
        LicenceOrQualification,
        LanguageSkill,
    ]
    if request.user.is_authenticated:
        return redirect('/projects/curriculum-vitae/mycv')
    else:
        if request.method == "POST":
            forms = registerUser(request.POST or None)
            if forms.is_valid():
                user = forms.save()
                group = Group.objects.get(name='CurriculumVitae')
                user.groups.add(group)
                personalData = PersonalData(personal_user=user, email=forms.cleaned_data['email'])
                for model in modelDataUser:
                    dataModel = model(personal_user=user)
                    dataModel.save()
                personalData.save()
                username = forms.cleaned_data['username']
                password = forms.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)

                return redirect('createCV')
        else:
            forms = registerUser()

    context = {
        'forms': forms,
    }


    return render(request, 'CurriculumVitae/register-index.html', context)

def Logout(request):
    logout(request)
    return redirect('/projects/curriculum-vitae/')




