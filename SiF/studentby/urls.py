from django.urls import path
from . import views

app_name = 'oversikt'
urlpatterns = [
    path('<int:studentby_id>', views.index, name='studentbyIndex'),
]
