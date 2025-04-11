from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base_html, name="Base"),
    path('', views.home, name="Home"),
    path('<int:id>', views.list, name="list"),
    path('create/', views.create, name="create"),
    path('view/', views.view, name="create"),
]