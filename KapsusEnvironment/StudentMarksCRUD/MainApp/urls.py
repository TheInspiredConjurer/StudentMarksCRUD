from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentListView.as_view(), name="StudentHome"),
    path('create/', CreateNewStudentView.as_view(), name="CreateNewStudent"),
    path('update/<int:pk>', UpdateStudentView.as_view(), name="UpdateStudent"),
    path('delete/<int:pk>', DeleteStudentView.as_view(), name="DeleteStudent"),
    path('marks/add/<int:pk>', AddMarksForSingleStudentView.as_view(), name="AddMarksForSingleStudent"),
    path('marks/update/<int:pk>', UpdateMarksForSingleStudentView.as_view(), name="UpdateMarksForSingleStudent"),
    path('marks/delete/<int:pk>', DeleteMarksForSingleStudentView.as_view(), name="DeleteMarksForSingleStudent"),
    path('marks/all', AllStudentsMarksView.as_view(), name="MarksOfAllStudents"),
]