from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
from django.shortcuts import redirect
from hello_world.models import BlogPost, Comment
from django.urls import reverse


# Create your views here.
def profile(request, username):
    """
    A view to display a user's profile, and update it if the user is logged in
    """
    profile = get_object_or_404(Profile, user__username=username)
    user = profile.user  # Define the user variable from the profile

    # Generate profile URL dynamically
    profile_url = reverse('profile', args=[username])

    posts = BlogPost.objects.filter(writer=user).order_by("created_at")
    comments = Comment.objects.filter(commenter=user).order_by("created_at")

    if request.method == "POST":
        if request.user.username != username:
            return redirect("profile", username=username)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile", username=username)
    else:
        profile_form = ProfileForm(instance=profile)

    context = {
        "profile": profile,
        "profile_form": profile_form,
        "posts": posts,
        "comments": comments,
        "profile_url": profile_url,  # Pass profile_url to the context
    }

    return render(request, "user_profile/profile.html", context)

def delete_account(request):
    if request.method == "POST":
        request.user.delete()
        # Redirect to home page
        return redirect("home")
    else:
        # Render the confirmation template
        return render(request, "delete_confirm.html")