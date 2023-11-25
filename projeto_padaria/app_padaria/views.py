from django.shortcuts import render
from .models import Cliente


# Create your views here.
def home(request):
    return render(request, "padaria/home.html")


def clientes(request):
    novo_cliente = Cliente()
    novo_cliente.nome = request.POST.get("nome")
    novo_cliente.telefone = request.POST.get("telefone")
    novo_cliente.save()

    # Exibir todos os clientes
    clientes = {"clientes": Cliente.objects.all()}

    # Retomar os dados
    return render(request, "padaria/clientes.html", clientes)
