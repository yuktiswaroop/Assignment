from django import forms
from .models import Post
from bootstrap_datepicker_plus import DatePickerInput

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
		
		widgets = {
			'created_at' : DatePickerInput(),
			'user': forms.TextInput(attrs={'disabled': True}),
		}
		
#https://pypi.org/project/django-bootstrap-datepicker-plus/	
