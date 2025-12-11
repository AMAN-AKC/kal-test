from django.db import models

GRADE_CHOICES = [
    ('O', 'O'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('F', 'F'),
]

class Student(models.Model):
    usn = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)
    semester = models.PositiveSmallIntegerField()
    subject_code = models.CharField(max_length=20, blank=True)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)

    def __str__(self):
        return f"{self.usn} - {self.name} ({self.grade})"
