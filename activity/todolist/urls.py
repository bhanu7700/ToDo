from .views import HomeView, AddPostView
from django.urls import path

urlpatterns = [
    path('',HomeView,name="home"),
    path('addpost/',AddPostView.as_view(), name='addpost')
]