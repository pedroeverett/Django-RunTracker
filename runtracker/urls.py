from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formm', views.newForm, name='formm'),
    path('add', views.addRun, name='add')
]