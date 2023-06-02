from django.shortcuts import render
from .forms import UserForm, JobSeekerForm, EducationForm, SkillForm, DocumentForm
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

# Create your views here.

class UserFormView(SessionWizardView):
    template_name = 'user_form.html'
    form_list = [UserForm, JobSeekerForm, EducationForm, SkillForm, DocumentForm]
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'documents'))

    def done(self, form_list, **kwargs):
        user_form = form_list[0]
        job_seeker_form = form_list[1]
        education_form = form_list[2]
        skill_form = form_list[3]
        document_form = form_list[4]

        user_form.save(commit=False)
        job_seeker_form.save(commit=False)
        education_form.save(commit=False)
        skill_form.save(commit=False)
        document_form.save(commit=False)

        user = user_form.save()
        job_seeker = job_seeker_form.save(commit=False)
        job_seeker.user = user
        job_seeker.save()

        education = education_form.save(commit=False)
        education.job_seeker = job_seeker
        education.save()

        skill = skill_form.save(commit=False)
        skill.job_seeker = job_seeker
        skill.save()

        document = document_form.save(commit=False)
        document.job_seeker = job_seeker
        document.save()

        return HttpResponseRedirect('/success/')

