from django.contrib import admin

from .models import Ticket, Comment


class LITReviewAdminiSite(admin.AdminSite):
    site_header = 'LITReview BackOffice'


admin_site = LITReviewAdminiSite(name='admin')

# @admin.register(Comment, site=admin_site)
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0 


# @admin.register(Ticket, site=admin_site)
class TicketAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin_site.register(Ticket, TicketAdmin)
admin_site.register(Comment)
