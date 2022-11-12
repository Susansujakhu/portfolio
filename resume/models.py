from django.db import models

# Create your models here.
class Downloads(models.Model):
    years = [
        ("1", "First"),
        ("2", "Second"),
        ("3", "Third"),
        ("4", "Fourth"),
    ]
    semesters = [
        ("I", "First"),
        ("II", "Second"),
        ("III", "Third"),
        ("IV", "Fourth"),
        ("V", "Fifth"),
        ("VI", "Sixth"),
        ("VII", "Seventh"),
        ("VIII", "Eighth"),
    ]
    types = [
        ("Notes", "Notes"),
        ("Question", "Question"),
        ("Syllabus", "Syllabus"),
    ]
    year = models.CharField(blank=False, max_length=10, choices=years)
    semester = models.CharField(blank=False, max_length=10, choices=semesters)
    subject = models.CharField(max_length=50)
    type = models.CharField(blank=False, max_length=10, choices=types)
    download_link = models.FileField(upload_to="documents")
    
    def __str__(self):
        return self.subject