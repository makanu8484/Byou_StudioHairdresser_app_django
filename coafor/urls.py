from django.urls import path

from coafor import views




urlpatterns = [
    path('create_booking_coafor', views.CoaforCreateView.as_view(), name='create_booking_coafor'),
    path('list_booking_coafor', views.CoaforListView.as_view(), name='list_booking_coafor'),
    path('update_booking_coafor/<int:pk>/', views.CoaforUpdateView.as_view(), name='update_booking_coafor'),
    path('delete_booking_coafor/<int:pk>/', views.CoaforDeleteView.as_view(), name='delete_booking_coafor'),
    path('details_booking_coafor/<int:pk>/', views.CoaforDetailView.as_view(), name='details_booking_coafor'),

]
