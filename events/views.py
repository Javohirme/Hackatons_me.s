from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import OuterRef, Exists
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from events.forms import CreateIdeaForm
from events.models import *


@login_required(login_url="/accounts/login/")
def home_page(request):
    now = timezone.now()
    active_hackathons = Event.objects.filter(
        is_approved=True, start_date__lt=now, end_date__gt=now
    )

    past_hackathons = Event.objects.filter(is_approved=True, end_date__lt=now)

    upcoming_hackathons = Event.objects.filter(is_approved=True, start_date__gt=now)

    return render(
        request,
        "home.html",
        context={
            "active_hackathons": active_hackathons,
            "upcoming_hackathons": upcoming_hackathons,
            "past_hackathons": past_hackathons,
        },
    )


class EventDetailView(View):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse("Event does not exist")

        ideas = event.ideas.annotate(
            is_liked=Exists(
                IdeaUpvote.objects.filter(user=request.user, idea=OuterRef("pk"))
            )
        )
        context = {"event": event, "idea_form": CreateIdeaForm(), "ideas": ideas}

        return render(request, "events/event_detail.html", context=context)


class CreateEventIdeaView(LoginRequiredMixin, View):
    def post(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return HttpResponse("Event does not exist")

        form = CreateIdeaForm(request.POST)

        if form.is_valid():
            Idea.objects.create(
                owner=request.user,
                event=event,
                title=form.cleaned_data["title"],
                overview=form.cleaned_data["overview"],
            )

        return redirect("events:event-detail", event_id=event_id)


class UpvoteIdeaView(LoginRequiredMixin, View):
    def post(self, request, event_id, idea_id):
        try:
            idea = Idea.objects.get(id=idea_id, event__id=event_id)
        except Idea.DoesNotExist:
            return HttpResponse("Idea does not exist")

        IdeaUpvote.objects.create(
            idea=idea,
            user=request.user,
        )

        return redirect("events:event-detail", event_id=event_id)


class DeleteIdeaView(LoginRequiredMixin, View):
    def post(self, request, idea_id):
        try:
            idea = Idea.objects.get(id=idea_id)
        except Idea.DoesNotExist:
            return HttpResponse("Idea does not exist", status=404)

        if idea.owner != request.user:
            return HttpResponseForbidden("You are not the owner of this idea")

        # G‘oyani o‘chirish
        idea.delete()

        return redirect("events:event-detail", event_id=idea.event.id)


# ==================


class UpvoteIdeaView(LoginRequiredMixin, View):
    def post(self, request, event_id, idea_id):
        try:
            idea = Idea.objects.get(id=idea_id, event__id=event_id)
        except Idea.DoesNotExist:
            return HttpResponse("Idea does not exist")

        # Yangi Upvote qo‘shish yoki o‘chirish
        upvote, created = IdeaUpvote.objects.get_or_create(idea=idea, user=request.user)

        if not created:
            upvote.delete()  # Agar allaqachon like bosilgan bo‘lsa, o‘chirish

        # Foydalanuvchini o‘sha eventning detail sahifasiga qaytarish
        return redirect("events:event-detail", event_id=event_id)
