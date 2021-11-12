from django.contrib import admin

from .models import Ticket, TicketReview

# from django import template
# register=template.Library()


class LITReviewAdminiSite(admin.AdminSite):
    site_header = 'LITReview BackOffice'


admin_site = LITReviewAdminiSite(name='admin')

# @admin.register(TicketReview, site=admin_site)
class TicketReviewInline(admin.TabularInline):
    model = TicketReview
    extra = 0 


# @admin.register(Ticket, site=admin_site)
class TicketAdmin(admin.ModelAdmin):
    inlines = [
        TicketReviewInline,
    ]


admin_site.register(Ticket, TicketAdmin)
admin_site.register(TicketReview)
