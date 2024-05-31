from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

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



    def get_queryset(self):
        return Manipedi.objects.all()


