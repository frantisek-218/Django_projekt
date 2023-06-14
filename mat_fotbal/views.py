from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import MatFotbalForm
from .models import Klub, Liga

def index(request):
    zanr = 'Kluby'
    context = {
        'nadpis': zanr,
        'kluby': Klub.objects.order_by('zalozeni'),
        'ligy': Liga.objects.all()
    }
    return render(request, 'index.html', context=context)

class KlubListView(ListView):
    model = Klub
    context_object_name = "kluby"
    template_name = "klub/klub_list.html"

class KlubDetailView(DetailView):
    model = Klub
    context_object_name = "klub"
    template_name = "klub/klub_detail.html"
        
