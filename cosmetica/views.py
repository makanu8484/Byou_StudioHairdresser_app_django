from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from cosmetica.forms import CosmeticaForm, CosmeticaUpdateForm
from cosmetica.models import Cosmetica


class CosmeticaCreateView(CreateView):
    template_name = 'cosmetica/create_booking_cosmetica.html'
    form_class = CosmeticaForm
    success_url = reverse_lazy('home')


class CosmeticaListView(ListView):
    template_name = 'cosmetica/list_cosmetica.html'
    model = Cosmetica
    context_object_name = 'all_list_cosmetica'


class CosmeticaUpdateView(UpdateView):
    template_name = 'cosmetica/update_booking_cosmetica.html'
    model = Cosmetica
    form_class = CosmeticaUpdateForm
    success_url = reverse_lazy('list_cosmetica')


class CosmeticaDeleteView(DeleteView):
    template_name = 'cosmetica/delete_booking_cosmetica.html'
    model = Cosmetica
    success_url = reverse_lazy('list_cosmetica')


class CosmeticaDetailView(DetailView):
    template_name = 'cosmetica/details_booking_cosmetica.html'
    model = Cosmetica





    def get_queryset(self):
        return Cosmetica.objects.all()

