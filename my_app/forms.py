from django import forms

from .models import *


class ShortURLForm(forms.ModelForm):

	class Meta:
		model= ShortURL		
		fields=['url',]

		widgets={
			'url': forms.URLInput(attrs={'class':'form-control'})

		}