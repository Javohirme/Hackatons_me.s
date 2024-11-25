from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static

AUTH_USER_MODEL = "users.CustomUser"


class Event(BaseModel):
    organizer = models.ForeignKey(
        "accounts.CustomUser",
        on_delete=models.CASCADE,
        related_name="events",
        related_query_name="event",
    )

    title = models.CharField(_("title"), max_length=50)
    overview = models.TextField(_("overview"))
    summary = models.CharField(_("summary"), max_length=100, blank=True)
    image = models.ImageField(blank=True, upload_to="images", null=True)

    start_date = models.DateTimeField(_("start date"))
    end_date = models.DateTimeField(_("end date"))

    is_approved = models.BooleanField(default=False)

    def __str__(self):

        return self.title

    def save(self, *args, **kwargs):
        if not self.summary:
            self.summary = (
                self.overview[:97] + "..."
                if len(self.overview) > 100
                else self.overview
            )
        super().save(*args, **kwargs)

    def get_image_url(self):
        if self.image:
            return self.image.url
        return static("images/none_image.png")


class Idea(BaseModel):
    event = models.ForeignKey(
        Event, related_name="ideas", related_query_name="idea", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        "accounts.CustomUser",
        related_name="ideas",
        related_query_name="idea",
        on_delete=models.CASCADE,
    )
    title = models.CharField(_("title"), max_length=50)
    overview = models.TextField(_("overview"))

    summary = models.CharField(_("summary"), max_length=100, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.summary:
            self.summary = (
                self.overview[:97] + "..."
                if len(self.overview) > 100
                else self.overview
            )
        super().save(*args, **kwargs)


class IdeaUpvote(BaseModel):

    user = models.ForeignKey(
        "accounts.CustomUser",
        related_name="upvotes",
        related_query_name="upvote",
        on_delete=models.CASCADE,
    )

    idea = models.ForeignKey(
        Idea,
        related_name="upvotes",
        related_query_name="upvote",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("idea", "user")

    def __str__(self):
        return f"{self.user} likes {self.idea.title}"
