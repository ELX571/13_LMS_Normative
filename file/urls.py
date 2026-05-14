from django.urls import path

from file import views

urlpatterns = [
    path('list/', views.file_list, name='file_list'),

]