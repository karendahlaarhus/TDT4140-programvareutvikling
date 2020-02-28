from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'vaskeliste'
urlpatterns = [
    path('<int:vaskeliste_id>', views.index, name='todoIndex'),
    path('addTodo', views.addTodo, name='addTodo'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]
