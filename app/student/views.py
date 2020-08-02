from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from .forms import StudentForm

from .models import Student

class StudentList(ListView):
	model = Student
	template_name = 'index.html'

class StudentCreate(CreateView):
	model = Student
	template_name = "CreateStudent.html"
	form_class = StudentForm
	success_url = reverse_lazy("index")

class StudentUpdate(UpdateView):
	model = Student
	template_name = "CreateStudent.html"
	form_class = StudentForm
	success_url = reverse_lazy("index")

class StudentDelete(DeleteView):
	model = Student 
	template_name = "Confirm.html"
	success_url = reverse_lazy('index')

