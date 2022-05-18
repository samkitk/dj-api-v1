from django.urls import path
from .views import DetailToDo,ListToDo,AddToDo

urlpatterns = [
    path("<int:pk>/", DetailToDo.as_view()),
    path('',ListToDo.as_view()),
    path('add',AddToDo.as_view())
]
