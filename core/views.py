from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    """View para a página inicial do sistema"""
    return render(request, 'core/home.html')

def base_view(request):
    """View para o template base (se necessário)"""
    return render(request, 'core/base.html')