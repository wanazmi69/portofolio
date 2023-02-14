from django.forms import ModelForm, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import PersonalData, BacgroundSchool, WorkHistory, LicenceOrQualification, LanguageSkill




class registerUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        


class FormPersonalData(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = '__all__'
        exclude = ['personal_user']
        fk_name = 'personal_user'
class FormBacgroundSchool(forms.ModelForm):
    class Meta:
        model = BacgroundSchool
        fields = '__all__'
        exclude = ['personal_user']
        fk_name = 'personal_user'

class FormWorkHistory(forms.ModelForm):
    class Meta:
        model = WorkHistory
        fields = '__all__'
        exclude = ['personal_user']
        fk_name = 'personal_user'

class FormLicenceOrQualification(forms.ModelForm):
    class Meta:
        model = LicenceOrQualification
        fields = '__all__'
        exclude = ['personal_user']

class FormLanguageSkill(forms.ModelForm):
    class Meta:
        model = LanguageSkill
        fields = '__all__'
        exclude = ['personal_user']



# class CreateUserProfile(forms.Form):
#     user_form = registerUser(prefix='user')
#     pesronalData_form = FormPersonalData(prefix='personal_data')
#     bacgroundSchool = FormBacgroundSchool(prefix='backgroud_scholl')
#     workHistory = FormWorkHistory(prefix='work_history')
#     licenceOrQualification = FormLicenceOrQualification(prefix='licence_qualification')
#     LanguageSkill = FormLanguageSkill(prefix='language_skill')




PersonaDataForm_set = inlineformset_factory(User, PersonalData, form=FormPersonalData, can_delete=False, extra=0)
BacgroundSchoolForm_set = inlineformset_factory(User, BacgroundSchool, form=FormBacgroundSchool, can_delete=False, extra=0)
WorkHistoryForm_set = inlineformset_factory(User, WorkHistory, form=FormWorkHistory, can_delete=False, extra=0)
LicenceOrQualificationForm_set = inlineformset_factory(User, LicenceOrQualification, form=FormLicenceOrQualification, can_delete=False, extra=0)
LanguageSkillForm_set = inlineformset_factory(User, LanguageSkill, form=FormLanguageSkill, can_delete=False, extra=0)



    
      


    
