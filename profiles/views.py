from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Profile



def follow_unfollow_profile(request):
    """function to unfollow"""
    if request.method=="POST":
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)
        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:profile-list-view')
    

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
