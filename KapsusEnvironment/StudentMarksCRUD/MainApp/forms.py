from dataclasses import fields
from django.forms import ModelForm, NumberInput, Select, TextInput

from .models import Student, Marks

class NewStudentCreationForm(ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'department_name']


class NewMarksAddingForm(ModelForm):
    class Meta:
        model = Marks
        fields = ['subject', 'marks', 'student']


class MarksUpdateForm(ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject', 'marks']
        widgets={'student': Select(attrs={'readonly': True}),
        'subject': TextInput(attrs={'readonly': True}),
        'marks': NumberInput(attrs={'min': 0, "max": 100})
        }