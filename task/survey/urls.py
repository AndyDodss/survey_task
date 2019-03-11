from django.urls import path,include
from . import views

urlpatterns = [
    path('myadmin', views.index, name='index' ),
    path('create/', views.create, name='create' ),
    path('add_question/', views.add_question, name='add_question' ),
    path('delete/<id>/', views.delete, name='delete' ),
    path('register', views.register, name='register' ),
     path('login_check', views.login_check, name='login_check' ),
     path('answer',views.answer,name='answer'),
    path('ans', views.ans, name='ans' ),



]