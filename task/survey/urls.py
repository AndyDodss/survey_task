from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('create/', views.create, name='create' ),
    path('add_question/', views.add_question, name='add_question' ),
    path('delete/<id>/', views.delete, name='delete' ),

    path('ans/', views.ans, name='ans' ),

]