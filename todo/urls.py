from django.urls import path
from .views import *

##For API
#TodoList
#TodoDetail


urlpatterns = [
    path('', index, name='index'),
    path('fetch/', todo_fetch, name='fetch'),
    path('save/', todo_save, name='save'),
    #path('todo/', TodoList.as_view()),
    #path('todo/<int:pk>/', TodoDetail.as_view()),
]




