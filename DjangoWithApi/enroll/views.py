from django.shortcuts import render
from .forms import StudentRegistration
# from .models import Student

# Create your views here.

def showstudentdata(req):
    if req.method == 'POST':
      fm = StudentRegistration(req.POST)
      if fm.is_valid():
         fm.cleaned_data['name']
         fm.cleaned_data['email']
         fm.cleaned_data['password']
         fm.cleaned_data['gender']
         fm.save()
    else:
        fm = StudentRegistration()
    return render(req, 'enroll/Registration.html', {'form':fm})


