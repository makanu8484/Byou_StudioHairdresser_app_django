from django.urls import path

from users import views


urlpatterns = [
    path('create_user/', views.UserCreate.as_view(), name='create_user'),
]