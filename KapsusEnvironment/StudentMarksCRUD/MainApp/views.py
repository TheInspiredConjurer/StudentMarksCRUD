from urllib import request
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, \
    DeleteView, DetailView, FormView
from .models import *
from .forms import *
from django import forms


# Create your views here.


class StudentListView(ListView):
    model = Student
    template_name = 'mainApp/StudentList.html'
    queryset = Student.objects.all().order_by('id')
    context_object_name = 'student_list'


class CreateNewStudentView(CreateView):
    model = Student
    form_class = NewStudentCreationForm
    template_name = 'mainApp/CreateNewStudent.html'
    success_url = reverse_lazy('StudentHome')


class UpdateStudentView(UpdateView):
    model = Student
    template_name = 'mainApp/UpdateStudent.html'
    fields = ['student_name', 'department_name']
    success_url = reverse_lazy('StudentHome')


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'mainApp/DeleteStudent.html'
    success_url = reverse_lazy('StudentHome')



class AddMarksForSingleStudentView(FormView):
    model = Marks
    form_class = NewMarksAddingForm
    template_name = 'mainApp/AddMarksForSingleStudent.html'
    success_url = reverse_lazy('MarksOfAllStudents')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = Student.objects.get(pk=self.kwargs['pk'])
        ## student = Student.objects.get(pk=self.kwargs['pk'])
        ## context["marks"] = Marks.objects.filter(student=student)
        return context

    def form_valid(self, form):
        NewNewMarksAdddingForm = form.save()  
        print(NewMarksAddingForm.errors)
        print(NewNewMarksAdddingForm)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("in forminvalid")
        print(form.errors)
        if(form.errors):
            marks = NewMarksAddingForm(self.request.POST.get('Marks'))
            subject_name = NewMarksAddingForm(self.request.POST.get('Subject'))
            print(marks)
            print(subject_name)
            print(form.errors)
            print("invalid form")
        return self.render_to_response(self.get_context_data(form=form))



class UpdateMarksForSingleStudentView(UpdateView):
    model = Marks
    form_class = MarksUpdateForm
    template_name = 'mainApp/UpdateMarksForSingleStudent.html'
    success_url = reverse_lazy('MarksOfAllStudents')


class DeleteMarksForSingleStudentView(DeleteView):
    model = Marks
    template_name = 'mainApp/DeleteMarksForSingleStudent.html'
    success_url = reverse_lazy('StudentHome')


class AllStudentsMarksView(ListView):
    model = Marks
    template_name = 'mainApp/AllStudentsMarks.html'
    queryset = Marks.objects.all().order_by('id', 'student_id')
    context_object_name = 'marks_list'

