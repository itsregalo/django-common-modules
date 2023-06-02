from django import forms
from .models import User, JobSeeker, Education, Skill, Document


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


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['job_seeker']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['job_seeker']