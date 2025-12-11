from django.db import models

# Create your models here.

class Student(models.Model):
    usn = models.CharField(max_length=10, unique=True, verbose_name="USN")
    name = models.CharField(max_length=100, verbose_name="Name")
    subject_code = models.CharField(max_length=10, verbose_name="Subject Code")
    cie_marks = models.IntegerField(verbose_name="CIE Marks")
    
    def __str__(self):
        return f"{self.usn} - {self.name}"
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
