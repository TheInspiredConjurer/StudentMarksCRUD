from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
  student_name=models.CharField(max_length=255, db_column="student_name", null=False, unique=False)
  department_name=models.CharField(max_length=255, db_column="department_name", null=False, unique=False)
  created_on=models.DateTimeField(db_column="created_on", auto_now_add=True, null=True)
  updated_on=models.DateTimeField(db_column="updated_on", auto_now_add=False, auto_now=True, null=True)

  def __str__(self):
    return (f"Student: {self.student_name}")

  class Meta:
    db_table='student'

class Marks(models.Model):
  subject=models.CharField(max_length=255, db_column="subject", null=False, unique=False)
  marks=models.CharField(max_length=255, db_column="marks", null=False, unique=False)
  created_on=models.DateField(db_column="created_on", auto_now_add=True)
  updated_on=models.DateField(db_column="updated_on", auto_now_add=False, auto_now=True)
  student=models.ForeignKey(to=Student, db_column="student_name", null=True, unique=False, on_delete=models.SET_NULL)

  def __str__(self):
    return (f"{self.student.student_name} - Marks in {self.subject}")

  class Meta:
    db_table='marks'