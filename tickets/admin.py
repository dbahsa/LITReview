from django.contrib import admin

from .models import Ticket, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0 


class TicketAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment)
