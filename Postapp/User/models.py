from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.CharField(max_length=250)
	created_at = models.DateTimeField(default = timezone.now)
	updated_at = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.text

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})

	class Meta:
		app_label = 'User'