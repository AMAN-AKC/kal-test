from django.db import models

class ExamStudent(models.Model):
	usn = models.CharField(max_length=20, unique=True, verbose_name='USN')
	name = models.CharField(max_length=150, verbose_name='Name')
	semester = models.PositiveSmallIntegerField(verbose_name='Semester')
	fee_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, verbose_name='Exam Fee Amount')
	fee_paid = models.BooleanField(default=False, verbose_name='Fee Paid')

	def __str__(self):
		return f"{self.usn} - {self.name}"

	class Meta:
		verbose_name = 'Exam Student'
		verbose_name_plural = 'Exam Students'
