from django.shortcuts import render
from .models import Pessoa


# Create your views here.

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})


def salvar(request):
    vnome = request.POST.get("nome")
    vidade = request.POST.get("idade")
    Pessoa.objects.create(nome=vnome, idade=vidade)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})


def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == "POST":
        pessoa.nome = request.POST.get("nome")
        pessoa.idade = request.POST.get("idade")
        pessoa.save()
        return redirect(home)
    return render(request, "editar.html", {"pessoa": pessoa})

def delete(request, id):
    pessoa = Pessoa.objects.get(id = id)
    pessoa.delete()
    return redirect(home)

def salvar(request):
    vnome = request.POST.get("nome")
    vidade = request.POST.get("idade")
    Pessoa.objects.create(nome=vnome,idade=vidade)
    pessoas = Pessoa.objects.all()
    return render(request,"index.html",{"pessoas":pessoas})

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request,"index.html",{"pessoas":pessoas})
