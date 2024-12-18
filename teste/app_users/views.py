from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def cadastro(request):
	if request.method == "POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			print(form)
			return redirect('usuarios')
	else:
		form = UsuarioForm()

	return render(request, 'usuarios/index.html',{'form':form})

def usuarios(request):
	usuarios = Usuario.objects.all()
	return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})
