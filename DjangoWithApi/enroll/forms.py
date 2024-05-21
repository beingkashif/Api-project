from django import forms
from .models import Student

GENDER_CHOICES = [

    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')


]
class StudentRegistration(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Student
        fields = ['name', 'email', 'password', 'gender']
        labels = {'name':'Enter Your Name', 'email':'Enter Your Email', 'password':'Enter Strong Password'}
        widgets = {
         'name':forms.TextInput(attrs={'class':'form-control'}),
         'email':forms.EmailInput(attrs={'class':'form-control'}),
         'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
