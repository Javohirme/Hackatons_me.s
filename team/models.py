from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="destinations/")

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="team_photos/")
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
