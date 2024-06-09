from . import views
from django.urls import path, include

urlpatterns = [
    # Post list (hello_world) view
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # Include Django authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
]