from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from hello_world.models import BlogPost, Comment
from .forms import ProfileForm
from .models import Profile


# Create your views here.
def profile(request, username):
    """
    Display a user's profile and handle profile updates.

    Retrieves the profile for the given username and renders the profile page
    with associated blog posts and comments. Allows the logged-in user to
    update their profile information using a form and there avatar.

    Returns:
        HttpResponse: Rendered profile template or redirect response
        upon successful form submission.

    Raises:
        Http404: If no Profile matches the given username.
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
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile", username=username)
        else:
            # Form (avatar) is invalid, handle error message display
            avatar_errors = profile_form.errors.get('avatar')
            if avatar_errors:
                messages.error(
                    request,
                    avatar_errors.as_text(),
                    extra_tags='avatar-error'
                    )
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
    """
    Handle account deletion.

    Deletes the logged-in user's account permanently upon POST request.
    Renders a confirmation page for GET request.

    Returns:
        HttpResponse: Redirects to the home page upon successful account
         deletion or renders the delete confirmation template for GET request.
    """
    if request.method == "POST":
        try:
            request.user.delete()
            messages.success(request, "Account deleted successfully")
            return redirect("home")
        except Exception as e:
            messages.error(request, f"Failed to delete profile: {str(e)}")
    if request.user.username:
        return redirect('profile', username=request.user.username)
    else:
        return redirect('home')