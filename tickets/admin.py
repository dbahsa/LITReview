from django.contrib import admin

from .models import Ticket, ReviewRating #, UserFollows

# from django import template
# register=template.Library()


class LITReviewAdminiSite(admin.AdminSite):
    site_header = 'LITReview BackOffice'


admin_site = LITReviewAdminiSite(name='admin')

class ReviewRatingInline(admin.TabularInline):
    model = ReviewRating
    extra = 0 


class TicketAdmin(admin.ModelAdmin):
    inlines = [
        ReviewRatingInline,
    ]


admin_site.register(Ticket, TicketAdmin)
admin_site.register(ReviewRating)
# admin_site.register(UserFollows)
