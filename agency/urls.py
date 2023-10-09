from django.urls import path

from .views import (
    index,
    TopicListView,
    TopicDetailView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperDeleteView,
    NewspaperUpdateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-info"),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path("redactors/<int:pk>/update/", RedactorUpdateView.as_view(), name="redactor-update"),
    path("redactors/<int:pk>/delete/", RedactorDeleteView.as_view(), name="redactor-delete"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"
    ),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path(
        "newspapers/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
    path(
        "newspapers/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),
]

app_name = "agency"
