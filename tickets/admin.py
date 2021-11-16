from django.contrib import admin

from .models import Ticket, Review, UserFollows

# from django import template
# register=template.Library()


class LITReviewAdminiSite(admin.AdminSite):
    site_header = 'LITReview BackOffice'


admin_site = LITReviewAdminiSite(name='admin')

# @admin.register(Review, site=admin_site)
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0 


# @admin.register(Ticket, site=admin_site)
class TicketAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]


admin_site.register(Ticket, TicketAdmin)
admin_site.register(Review)
admin_site.register(UserFollows)
