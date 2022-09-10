from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.urls import reverse
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default = 'profile.jpg', upload_to='profile_pictures')
    position = models.CharField(max_length=50)
    bio = models.TextField()
    detailed_bio = models.TextField()
    dob = models.DateField(default = '1999-01-01', auto_now=False, auto_now_add=False)
    address = models.CharField(default = "Nepal", max_length=100)
    zip = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    git = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username

class Education(models.Model):
    level_choice = [
        ("Bachelors (or equivalent)", "Bachelors (or equivalent)"),
        ("Masters (or equivalent)", "Masters (or equivalent)"),
        ("Doctorate (or equivalent)", "Doctorate (or equivalent)"),
        ("MBA (or equivalent)", "MBA (or equivalent)"),
        ("Secondary/High School (or equivalent)", "Secondary/High School (or equivalent)"),
        ("Other degree", "Other degree")
    ]

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    level = models.CharField(blank=False, max_length=50, choices=level_choice)
    degree = models.CharField(blank=False, max_length=100)
    college = models.CharField(blank=False, max_length=100)
    start_date = models.DateField(blank=False, auto_now=False, auto_now_add=False)
    end_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    still_enrolled = models.BooleanField(default=False)

    def __str__(self):
        return self.level


class WorkHistory(models.Model):
    emp_type_choices = [
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("Contract", "Contract"),
        ("Internship", "Internship"),
        ("Freelance", "Freelance"),
        ("Others", "Others")

    ]

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    position = models.CharField(blank=False, max_length=50)
    company = models.CharField(blank=False, max_length=50)
    employment_type = models.CharField(blank=False, max_length=50, choices=emp_type_choices) 
    start_date = models.DateField(blank=False, auto_now=False, auto_now_add=False)
    end_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    still_enrolled = models.BooleanField(default=False)

    def __str__(self):
        return self.company

class Project(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    work_place = models.ForeignKey(WorkHistory, on_delete=models.CASCADE, default=1, blank=True, null=True)
    project_name = models.CharField(blank=False, max_length=50)
    url_or_github_repo = models.CharField(blank=True, null=True, max_length=50) 
    start_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    still_enrolled = models.BooleanField(default=False)
    project_description = models.TextField(blank=False)
    project_outcome = models.TextField(blank=False)
    tech_stacks = models.CharField(blank=False, max_length=200)
    screenshots = models.ImageField(blank=True, null=True, upload_to='screenshots')

    def __str__(self):
        return self.project_name

class Trainings(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    training_name = models.CharField(blank=False, max_length=50)
    duration = models.CharField(blank=False, max_length=10)
    start_date = models.DateField(blank=False, auto_now=False, auto_now_add=False)
    end_date = models.DateField(blank=False, auto_now=False, auto_now_add=False)
    certificate = models.ImageField(blank=True, null=True, upload_to='certificates')

    def __str__(self):
        return self.training_name


class Skill(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    name = models.CharField(blank=False, max_length=50)
    percent = models.IntegerField(blank=False, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)])
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Contact(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(blank=False, max_length=200)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name+" / "+self.email

    def get_absolute_url(self):
        return reverse('resume:index')