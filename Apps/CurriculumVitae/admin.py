from django.contrib import admin

# Register your models here.
from .models import PersonalData, BacgroundSchool, WorkHistory, LicenceOrQualification, LanguageSkill

admin.site.register(PersonalData)
admin.site.register(BacgroundSchool)
admin.site.register(WorkHistory)
admin.site.register(LicenceOrQualification)
admin.site.register(LanguageSkill)