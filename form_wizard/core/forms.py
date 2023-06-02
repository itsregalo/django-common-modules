from django import forms
from .models import User, JobSeeker, Education, Skill, Document
from django.forms import formset_factory


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        exclude = ['user']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['job_seeker']

        widgets = {
            'certificate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your certificate'}),
            'institute': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your institute'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['job_seeker']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['job_seeker']

