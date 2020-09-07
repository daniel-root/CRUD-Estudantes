from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request,template='students/student_list.html'):
    studants = Student.objects.all()
    return render(request,template,{'alunos':studants})
def student_create(request, template='students/student_form.html'):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:        
        form = StudentForm()
    return render(request,template,{'form':form})    
    
def student_read(request, pk, template='students/student_read.html'):
    student = Student.objects.get(pk=pk)
    return render(request,template,{'aluno':student})    

def student_update(request, pk, template='students/student_form.html'):
    student = Student.objects.get(pk = pk)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:        
        form = StudentForm(instance=student)
    return render(request,template,{'form':form})

def student_delete(request, pk, template='students/student_delete.html'):
    student = Student.objects.get(pk = pk)
    if request.method == 'POST':
        student.delete()
        return redirect('/')
    else:
        return render(request,template,{'aluno':student})    