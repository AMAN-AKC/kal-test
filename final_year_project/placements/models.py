from django.db import models

class Placement(models.Model):
    usn = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.usn} - {self.name} @ {self.company}"
