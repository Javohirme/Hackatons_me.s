from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("team/", views.team_page, name="team"),
    path("support/", views.support_page, name="support"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("destinations/", views.destinations_list, name="destinations"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
