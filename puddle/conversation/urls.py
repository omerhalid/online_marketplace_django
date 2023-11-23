from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'), # inbox
    path('<int:pk>/', views.detail, name='detail'), # conversation detail (messages
    path('new/<int:item_pk>/', views.new_conversation, name='new'), # new conversation
]