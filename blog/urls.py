from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.detail, name='detail'),
    path('<slug:slug>/', views.display, name='display'),
    path('<slug:slug>/', views.show, name='show')
] 