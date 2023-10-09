from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RedactorSearchForm, NewspaperSearchForm, RedactorCreationForm, RedactorUpdateForm
from .models import Topic, Redactor, Newspaper


@login_required
def index(request):
    """View function for the home page of the site."""

    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()

    context = {
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
    }

    return render(request, "agency/index.html", context=context)


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = "newspaper_list"
    template_name = "agency/newspaper_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get("title")
        if title:
            return queryset.filter(title__icontains=title)
        return queryset


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"

    def get_success_url(self):
        return reverse(
            "agency:newspaper-detail",
            kwargs={"pk": self.object.pk},
        )


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"

    def get_success_url(self):
        return reverse(
            "agency:newspaper-detail",
            kwargs={"pk": self.object.pk},
        )


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = NewspaperSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.GET.get("username")
        if username:
            return queryset.filter(name__icontains=username)
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm

    def get_success_url(self):
        return reverse(
            "agency:redactor-info",
            kwargs={"pk": self.object.pk},
        )


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm

    def get_success_url(self):
        return reverse(
            "agency:redactor-info",
            kwargs={"pk": self.object.pk},
        )


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 20


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")
    fields = "__all__"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"

    def get_success_url(self):
        return reverse(
            "agency:topic-detail",
            kwargs={"pk": self.object.pk},
        )


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")
