from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField

# Create your models here.

class PersonalData(models.Model):
    gender_choice = (
        ('男','Male'),
        ('女','Female')
    )
    pairs_choice = (
        ('Yes','Yes'),
        ('No','No'),
    )
    support_obligation_choice = (
        ('Yes','Yes'),
        ('No','No')
    )
    personal_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = ResizedImageField(force_format='WEBP', quality=85, blank=True, null=True, upload_to='images/%Y/%m/%d/', max_length=200)
    full_name = models.CharField(max_length=30, null=True, blank=True)
    furigana = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)

    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(choices=gender_choice, max_length=6, null=True, blank=True)

    country = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    current_address = models.CharField(max_length=100, null=True, blank=True)
    current_address_furigana = models.CharField(max_length=100, null=True, blank=True)
    status_of_residence = models.CharField(max_length=100, null=True, blank=True, default='技術・人文知識・国際業務')
    period_of_stay = models.DateField(null=True, blank=True)

    default_language = models.CharField(max_length=200, null=True, blank=True)
    hobbie = models.CharField(max_length=20, null=True, blank=True)
    dependens = models.IntegerField(null=True, blank=True)
    pairs = models.CharField(choices=pairs_choice, null=True, blank=True, max_length=5, default='No')
    spouse_support_obligation = models.CharField(choices=support_obligation_choice, null=True, blank=True, max_length=5, default='No')

    Reason_for_coming = models.TextField(max_length=1000, null=True, blank=True)
    motifation = models.TextField(max_length=1000, null=True, blank=True)
    request = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.full_name, self.email)

    




class LanguageSkill(models.Model):
    japanese_level_choices = (
        ('N5','N5'),
        ('N5 勉強中','N5 勉強中'),
        ('N4','N4'),
        ('N4 勉強中','N4 勉強中'),
        ('N3','N3'),
        ('N3 勉強中','N3 勉強中'),
        ('N2','N2'),
        ('N2 勉強中','N2 勉強中'),
        ('N1','N1'),
        ('N1 勉強中','N1 勉強中'),
    )
    english_level_choices = (
        ('Business','Business'),
        ('Fluent','Fluent'),
        ('Conversational','Conversational'),
    )
    personal_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    japanese_level = models.CharField(choices=japanese_level_choices, max_length=20, null=True, blank=True)
    english_level = models.CharField(choices=english_level_choices, max_length=20, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.personal_user, self.japanese_level)


class BacgroundSchool(models.Model):

    personal_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    admission_year = models.IntegerField(null=True, blank=True)
    admission_month = models.IntegerField(null=True, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)
    graduation_month = models.IntegerField(null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return '%s %s' % (self.personal_user, self.education)
   


class WorkHistory(models.Model):
    part_time_choice = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    personal_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    join_year = models.IntegerField(null=True, blank=True)
    join_month = models.IntegerField(null=True, blank=True)
    leave_year = models.IntegerField(null=True, blank=True)
    leave_month = models.IntegerField(null=True, blank=True)
    work = models.CharField(max_length=100, null=True, blank=True)
    part_time = models.CharField(choices=part_time_choice,  max_length=5, null=True, blank=True, default='No')

    def __str__(self):
        return '%s %s' % (self.personal_user, self.work)


class LicenceOrQualification(models.Model):
    personal_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    license_or_qualification = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.personal_user, self.license_or_qualification)
















    













    # def __str__(self):
    #     return '%s' % (self.full_name)