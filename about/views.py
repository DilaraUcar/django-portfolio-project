from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the About page.

    This view retrieves the most recently updated About
    object from the database and renders the 'about/about.html' template,
    passing the About object as context.

    **Context**
    - ``about``: The most recent instance of :model:`about.About`.

    **Template**
    - :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_at').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
