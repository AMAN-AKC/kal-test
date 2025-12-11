from django.db import models

class Student(models.Model):
    usn = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)
    dept = models.CharField(max_length=100)
    grade = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f"{self.usn} - {self.name} ({self.dept})"