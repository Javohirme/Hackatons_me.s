from django.urls import path
from . import views
from .views import *

app_name = "events"

urlpatterns = [
    path("", views.home_page, name="home"),
    path(
        "<int:event_id>/",
        EventDetailView.as_view(),
        name="event-detail",
    ),
    path(
        "<int:event_id>/ideas/",
        CreateEventIdeaView.as_view(),
        name="create-idea",
    ),
    path(
        "<int:event_id>/ideas/<int:idea_id>",
        UpvoteIdeaView.as_view(),
        name="upvote-idea",
    ),
    path(
        "event/<int:event_id>/idea/<int:idea_id>/upvote/",
        views.UpvoteIdeaView.as_view(),
        name="upvote-idea",
    ),
    path(
        "idea/<int:idea_id>/delete/",
        DeleteIdeaView.as_view(),
        name="delete-idea",
    ),
]
