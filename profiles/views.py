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
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/detail.html'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context["follow"] = follow
        return context
