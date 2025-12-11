from django.db import models

TITLE_CHOICES = [
    ('Professor', 'Professor'),
    ('Associate Professor', 'Associate Professor'),
    ('Assistant Professor', 'Assistant Professor'),
    ('Lecturer', 'Lecturer'),
]

class Faculty(models.Model):
    faculty_id = models.CharField(max_length=20, primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=30, choices=TITLE_CHOICES)
    name = models.CharField(max_length=150)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.faculty_id} - {self.name} ({self.title})"
