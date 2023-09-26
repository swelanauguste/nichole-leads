from django.urls import path

from .views import (
    LeadCreateView,
    LeadDetailView,
    LeadListView,
    LeadStatusUpdateView,
    add_comment,
)

urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
    path("detail/<int:pk>/", LeadDetailView.as_view(), name="lead-detail"),
    path("update-status/<int:pk>/", LeadStatusUpdateView.as_view(), name="lead-status-update"),
    path("lead/<int:pk>/comment", add_comment, name="lead-add-comment"),
    path("create/", LeadCreateView.as_view(), name="lead-create"),
]
