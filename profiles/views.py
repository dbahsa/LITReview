from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/main.html'
    context_object_name = 'profiles' # object_list as default

    def get_queryset(self):
        # getting all the profiles w/o the one that belongs to the logged-in user
        return Profile.objects.all().exclude(user=self.request.user)

