from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.post_list, name='post_list'),
]