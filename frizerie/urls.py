from django.urls import path

from frizerie import views

urlpatterns = [
    path('create_booking_frizerie', views.FrizerieCreateView.as_view(), name='create_booking_frizerie'),
    path('list_booking_frizerie', views.FrizerieListView.as_view(), name='list_booking_frizerie'),
    path('update_booking_frizerie/<int:pk>', views.FrizerieUpdateView.as_view(), name='update_booking_frizerie'),
    path('details_booking_frizerie/<int:pk>', views.FrizerieDetailView.as_view(), name='details_booking_frizerie'),
    path('delete_booking_frizerie/<int:pk>', views.FrizerieDeleteView.as_view(), name='delete_booking_frizerie'),

]