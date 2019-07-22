from django.db import models

# Create your models here.
class Note(models.Model):
	title = models.CharField(max_length=90)
	body = models.TextField()

	def __str__(self):
		return self.title