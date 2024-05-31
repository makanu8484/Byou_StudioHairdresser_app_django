from django.urls import path

from cosmetica import views

urlpatterns = [
    path('create_booking_cosmetica', views.CosmeticaCreateView.as_view(), name='create_booking_cosmetica'),
    path('list_cosmetica', views.CosmeticaListView.as_view(), name='list_cosmetica'),
    path('update_booking_cosmetica/<int:pk>/', views.CosmeticaUpdateView.as_view(), name='update_booking_cosmetica'),

]