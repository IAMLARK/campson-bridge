from django import forms
from .models import Course, Lecturer
from django.contrib.auth.models import User

# Ensure you import the Lecturer model

class AddCourseForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "course", "class": "form-control"}),
        label=""
    )
    description = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Description", "class": "form-control"}),
        label=""
    )
    lecturer = forms.ModelChoiceField(
        queryset=Lecturer.objects.all(),
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        label=""
    )
  

    class Meta:
        model = Course
        exclude = ("user",)
