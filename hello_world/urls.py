from django.urls import path, include
from hello_world import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('post/<slug:slug>/comment/<int:comment_id>/edit/',
         views.comment_edit, name='comment_edit'),
    path('comment/<int:comment_id>/delete/',
         views.comment_delete, name='delete_comment'),
]
