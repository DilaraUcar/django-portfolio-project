from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/delete_account/',
         views.delete_account, name='delete_account'),
]
