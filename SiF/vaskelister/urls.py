from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
  #  path('', TemplateView.as_view(template_name='list_lists.html'), name='list_lists'),
    path('', views.index, name='test'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]
