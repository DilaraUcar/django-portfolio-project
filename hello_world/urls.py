from . import views
from django.urls import path

urlpatterns = [
    # Post list (hello_world) view
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]