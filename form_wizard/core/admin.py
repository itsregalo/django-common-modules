
from django.contrib import admin

from .models import User, JobSeeker, Education, Skill, Document

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_no')


# inlines
class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1


@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'state', 'pin_code')
    inlines = [EducationInline, SkillInline, DocumentInline]
