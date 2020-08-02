from django.db import models

# Create your models here.
class Student(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 120)
	course = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

