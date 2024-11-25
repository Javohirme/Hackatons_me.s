from django.urls import path, include
from . import views


urlpatterns = [
    # path("", include("events.urls"), name="home"),
    path("contact", views.home_view, name="contact"),
    path("about/", views.about, name="about"),
    path("success/", views.success_view, name="success"),
    
]
