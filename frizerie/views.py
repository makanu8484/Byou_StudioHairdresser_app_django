from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from frizerie.forms import FrizerieForm, FrizerieUpdateForm
from frizerie.models import Frizerie


class FrizerieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'frizerie/create_booking_frizerie.html'
    form_class = FrizerieForm
    success_url = reverse_lazy('home')


class FrizerieListView(LoginRequiredMixin,ListView):
    template_name = 'frizerie/list_booking_frizerie.html'
    model = Frizerie
    context_object_name = 'all_list_of_frizerie'



class FrizerieUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'frizerie/update_booking_frizerie.html'
    model = Frizerie
    form_class = FrizerieForm
    success_url = reverse_lazy('list_booking_frizerie')

    def get_queryset(self):
        return Frizerie.objects.all()





class FrizerieDetailView(LoginRequiredMixin,DetailView):
    template_name = 'frizerie/details_booking_frizerie.html'
    model = Frizerie





class FrizerieDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'frizerie/delete_booking_frizerie.html'
    model = Frizerie
    success_url = reverse_lazy('list_booking_frizerie')


    def get_queryset(self):
        return Frizerie.objects.all()

