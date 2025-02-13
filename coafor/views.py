from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from coafor.forms import CoaforForm, CoaforUpdateForm
from coafor.models import Coafor



class CoaforCreateView(LoginRequiredMixin, CreateView):
    template_name = 'coafor/create_booking_coafor.html'
    form_class = CoaforForm
    success_url = reverse_lazy('list_booking_coafor')


class CoaforListView(LoginRequiredMixin, ListView):
    template_name = 'coafor/list_booking_coafor.html'
    model = Coafor
    context_object_name = 'all_list_of_coafor'


class CoaforUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'coafor/update_booking_coafor.html'
    model = Coafor
    form_class = CoaforUpdateForm
    success_url = reverse_lazy('list_booking_coafor')

    def get_queryset(self):
        return Coafor.objects.all()


class CoaforDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'coafor/delete_booking_coafor.html'
    model = Coafor
    success_url = reverse_lazy('list_booking_coafor')


class CoaforDetailView(LoginRequiredMixin, DetailView):
    template_name = 'coafor/details_booking_coafor.html'
    model = Coafor

    def get_queryset(self):
        return Coafor.objects.all()
