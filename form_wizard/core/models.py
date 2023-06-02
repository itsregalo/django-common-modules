from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'user'
        verbose_name_plural = 'users'


class JobSeeker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email
    
    class Meta:
        db_table = 'job_seeker'
        verbose_name_plural = 'job_seekers'


class Education(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    certificate = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.job_seeker.user.email + ' - ' + self.certificate
    
    class Meta:
        db_table = 'education'
        verbose_name_plural = 'educations'


class Skill(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.job_seeker.user.email + ' - ' + self.skill
    
    class Meta:
        db_table = 'skill'
        verbose_name_plural = 'skills'


class Document(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    document = models.CharField(max_length=50)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.job_seeker.user.email + ' - ' + self.document
    
    class Meta:
        db_table = 'document'
        verbose_name_plural = 'documents'



    