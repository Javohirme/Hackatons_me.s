from django.shortcuts import render, redirect
from .forms import ContactForm


def home_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("success")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def success_view(request):
    return render(request, "success.html")


def about(request):
    return render(request, "about.html")



