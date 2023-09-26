from django.contrib import admin

from .models import Lead, LeadComment,  LeadType, LeadStatus


admin.site.register(LeadType)
admin.site.register(LeadComment)
admin.site.register(Lead)
admin.site.register(LeadStatus)
