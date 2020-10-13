from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Cliente

def listcliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'index.html', {'cliente':cliente})

def cadastrocliente(request):
    clienteformset = modelformset_factory(Cliente, fields=('__all__'))
    
    if request.method == 'POST':
        form = clienteformset(request.POST)
        instances = form.save(commit=False)
        
        for instance in instances:
            instance.save()
            return redirect('listcliente')
    
    form = clienteformset()

    return render(request, 'cadastro.html', {'form':form})

def editcliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    clienteformset = modelformset_factory(Cliente, fields=('__all__'))

    if request.method == 'POST':
        form = clienteformset(request.POST)

        instances = form.save(commit=False)
        
        for instance in instances:
            instance.save()
    
    form = clienteformset()

    return render(request, 'cadastro.html', {'form':form})

def deletcliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('listcliente')    




