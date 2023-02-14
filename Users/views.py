from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def loginUser(request):
    return render(request, 'Users/index.html')