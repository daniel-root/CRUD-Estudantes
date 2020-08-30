from django.shortcuts import render, redirect
from .models import Studant
from .forms import StudantForm

def studant_list(request, template='studants/studant_list.html'):
    alunos = Studant.objects.all()
    return render(request, template, {'alunos':alunos})

def studant_create(request, template='studants/studant_form.html'):
    if request.method == 'POST':
        form = StudantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudantForm()
    return render(request, template, {'form': form})

def studant_read(request, studant_id, template='studants/studant_read.html'):
    aluno = Studant.objects.get(id=studant_id)
    return render(request, template,{'aluno':aluno})

def studant_update(request, studant_id, template='studants/studant_form.html'):
    aluno = Studant.objects.get(id=studant_id)
    if request.method == 'POST':
        form = StudantForm(request.POST,instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudantForm(instance=aluno)
    return render(request, template, {'form': form})

def studant_delete(request, studant_id, template='studants/studant_delete.html'):
    aluno = Studant.objects.get(id=studant_id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('/')
    else:
        return render(request, template,{'aluno':aluno})