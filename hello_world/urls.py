from django.urls import path, include
from hello_world import views 

urlpatterns = [
    # Post list (hello_world) view
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # Include Django authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
    # URL for comment edit
    path('post/<slug:slug>/comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    #path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
     # URL for comment delete
    #path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
     path('comment/<int:comment_id>/delete/', views.comment_delete, name='delete_comment'),
     # URL for post delete
     #path('post/<int:post_id>/delete/', views.post_delete, name='delete_post'),
]
