from django.shortcuts import render
from .forms import UserForm, JobSeekerForm, EducationForm, SkillForm, DocumentForm
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.forms import formset_factory

# Create your views here.
JobSeekerEducationFormSet = formset_factory(EducationForm, extra=2)
JobSeekerSkillFormSet = formset_factory(SkillForm, extra=1)
JobSeekerDocumentFormSet = formset_factory(DocumentForm, extra=1)

class UserFormView(SessionWizardView):

    form_list = [
        ('user',UserForm),
        ('job_seeker',JobSeekerForm),
        ('education',JobSeekerEducationFormSet),
        ('skill',JobSeekerSkillFormSet),
        ('document',JobSeekerDocumentFormSet)
    ]

    # form templates for each step
    templates = {
        'user':'core/user_form.html',
        'job_seeker':'core/job_seeker_form.html',
        'education':'core/education_form.html',
        'skill':'core/skill_form.html',
        'document':'core/document_form.html'
    }
    file_storage = FileSystemStorage(location=settings.MEDIA_ROOT)

    def get_template_names(self):
        return [self.templates[self.steps.current]]
    
    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        step = self.steps.current

        # Pass formsets to the template context for the respective steps
        if step == 'education':
            context['formset'] = context['wizard']['form'].forms
        elif step == 'skill':
            context['formset'] = context['wizard']['form'].forms
        elif step == 'document':
            context['formset'] = context['wizard']['form'].forms

        return context

    def done(self, form_list, **kwargs):
        form_data = self.get_all_cleaned_data()
        user_form = form_list[0]
        job_seeker_form = form_list[1]
        education_form = form_list[2]
        skill_form = form_list[3]
        document_form = form_list[4]

        user = user_form.save(commit=False)
        user.set_password(user.password)
        user.save()

        job_seeker = job_seeker_form.save(commit=False)
        job_seeker.user = user
        job_seeker.save()

        for form in education_form:
            education = form.save(commit=False)
            education.job_seeker = job_seeker
            education.save()

        for form in skill_form:
            skill = form.save(commit=False)
            skill.job_seeker = job_seeker
            skill.save()

        for form in document_form:
            document = form.save(commit=False)
            document.job_seeker = job_seeker
            document.save()

        return HttpResponseRedirect('/success/')
