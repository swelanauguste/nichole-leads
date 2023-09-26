from django.db import models
from django.shortcuts import reverse


class LeadType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class LeadStatus(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Lead(models.Model):
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    lead_type = models.ForeignKey(
        LeadType,
        on_delete=models.SET_NULL,
        null=True,
        related_name="type_list",
        default=1,
    )
    status = models.ForeignKey(
        LeadStatus, on_delete=models.SET_NULL, null=True, related_name="status_list", default=1
    )
    source = models.CharField(max_length=255, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    email = models.EmailField(blank=True)
    ref_no = models.TextField(blank=True)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("lead-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class LeadComment(models.Model):
    lead = models.ForeignKey(
        Lead, on_delete=models.CASCADE, related_name="comments_list"
    )
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.lead.name}"
