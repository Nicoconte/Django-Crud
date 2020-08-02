from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		#fields = (dato, dato, dato, n dato)
		fields = "__all__"
