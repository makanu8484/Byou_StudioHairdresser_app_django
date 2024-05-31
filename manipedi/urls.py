from django.urls import path

from manipedi import views


urlpatterns = [

    path('create_booking_manipedi', views.ManipediCreateView.as_view(), name='create_booking_manipedi'),
    path('list_booking_manipedi', views.ManipediListView.as_view(), name='list_booking_manipedi'),
]