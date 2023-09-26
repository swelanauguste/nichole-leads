from django import forms

from .models import Lead, LeadComment


class LeadStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ("status",)


class LeadCreateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        widgets = {
            "ref_no": forms.Textarea(attrs={"rows": 4}),
            "note": forms.Textarea(attrs={"rows": 4}),
        }


class LeadCommentCreateForm(forms.ModelForm):
    class Meta:
        model = LeadComment
        fields = ("comment",)
        widgets = {
            "comment": forms.Textarea(
                attrs={"placeholder": "Write your comment here...", "rows": 4}
            ),
        }
