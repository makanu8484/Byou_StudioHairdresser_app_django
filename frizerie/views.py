from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from frizerie.forms import FrizerieForm
from frizerie.models import Frizerie


class FrizerieCreateView(CreateView):
    template_name = 'frizerie/create_booking_frizerie.html'
    form_class = FrizerieForm
    success_url = reverse_lazy('home')


class FrizerieListView(ListView):
    template_name = 'frizerie/list_booking_frizerie.html'
    model = Frizerie
    context_object_name = 'all_list_of_frizerie'


    def get_queryset(self):
        return Frizerie.objects.all()

