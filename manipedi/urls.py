from django.urls import path

from manipedi import views


urlpatterns = [

    path('create_booking_manipedi/', views.ManipediCreateView.as_view(), name='create_booking_manipedi'),
    path('list_booking_manipedi/', views.ManipediListView.as_view(), name='list_booking_manipedi'),
    path('update_booking_manipedi/<int:pk>', views.ManipediUpdateView.as_view(), name='update_booking_manipedi'),
    path('delete_booking_manipedi/<int:pk>', views.ManipediDeleteView.as_view(), name='delete_booking_manipedi'),
    path('details_booking_manipedi/<int:pk>', views.ManipediDetailView.as_view(), name='details_booking_manipedi'),

]