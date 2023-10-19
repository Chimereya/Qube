from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('ask/', views.ask_question, name='ask'),
    path('update/<int:pk>/', views.update_question, name='update'),
    path('delete<int:pk>/', views.delete_view, name='delete'),
    path('like_post/<int:pk>/', views.like_post, name='like_post'),
    path('comment/reply/', views.reply_post, name="reply"),
]