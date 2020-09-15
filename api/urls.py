# urls of the api
from django.urls import path, include
from . import views

urlpatterns = [

    #API
    path('todos', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoComplete.as_view()),
    path('todos/completed', views.TodoCompleteList.as_view()),


    # Auth
    path('signup', views.signup),
    path('login', views.login),

]


