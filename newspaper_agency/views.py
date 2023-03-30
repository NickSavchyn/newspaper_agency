from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# from newspaper_agency.forms import RedactorCreationForm, RedactorUpdateForm, NewspaperForm
from newspaper_agency.models import Topic, Newspaper, Redactor


@login_required
def index(request):
    """View function for the home page of th site"""

    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()
    new_redactors = Redactor.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
        "new_redactors": new_redactors,
        "num_visits": num_visits + 1
    }

    return render(request, "newspaper_agency/index.html", context=context)
