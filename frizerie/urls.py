from django.urls import path

from frizerie import views

urlpatterns = [
    path('create_booking_frizerie', views.FrizerieCreateView.as_view(), name='create_booking_frizerie'),
    path('list_booking_frizerie', views.FrizerieListView.as_view(), name='list_booking_frizerie')

]