from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'vaskeliste'
urlpatterns = [
    path('<int:vaskeliste_id>', views.index, name='todoIndex'),
    path('complete', views.completeTodo, name='complete'),
]
