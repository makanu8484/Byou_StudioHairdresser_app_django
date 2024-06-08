from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from manipedi.forms import ManipediForm
from manipedi.models import Manipedi


class ManipediCreateView(CreateView):
    template_name = 'manipedi/create_booking_manipedi.html'
    form_class = ManipediForm
    success_url = reverse_lazy('home')



class ManipediListView(ListView):
    template_name = 'manipedi/list_booking_manipedi.html'
    model = Manipedi
    context_object_name = 'all_list_manipedi'



class ManipediUpdateView(UpdateView):
    template_name = 'manipedi/update_booking_manipedi.html'
    form_class = ManipediForm
    success_url = reverse_lazy('list_booking_manipedi')

    def get_queryset(self):
        return Manipedi.objects.all()


class ManipediDeleteView(DeleteView):
    template_name = 'manipedi/delete_booking_manipedi.html'
    success_url = reverse_lazy('list_booking_manipedi')

    def get_queryset(self):
        return Manipedi.objects.all()


class ManipediDetailView(DetailView):
    template_name = 'manipedi/details_booking_manipedi.html'
    model = Manipedi
    success_url = reverse_lazy('list_booking_manipedi')




    def get_queryset(self):
        return Manipedi.objects.all()


