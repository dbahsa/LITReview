from django.contrib import admin
from .models import Profile

from tickets.admin import admin_site


admin_site.register(Profile)
# admin.site.register(Profile)
