from django.urls import path

from . import views
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('save_file/',views.save_file, name='save_file')
]