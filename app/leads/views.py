from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import LeadCommentCreateForm, LeadCreateForm, LeadStatusUpdateForm
from .models import Lead


class LeadListView(ListView):
    model = Lead

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LeadCreateForm()
        context["status_update_form"] = LeadStatusUpdateForm()
        return context


class LeadDetailView(DetailView):
    model = Lead

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LeadCommentCreateForm()
        return context


def add_comment(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == "POST":
        form = LeadCommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.lead = lead
            comment.save()
            return redirect(
                "lead-detail", pk=pk
            )  # Redirect back to the lead detail page
    else:
        form = LeadCommentCreateForm()
    return redirect("lead-detail", pk=pk)


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadCreateForm
    # success_url = reverse_lazy("lead-list")


class LeadStatusUpdateView(UpdateView):
    model = Lead
    form_class = LeadStatusUpdateForm
    success_url = reverse_lazy("lead-list")
