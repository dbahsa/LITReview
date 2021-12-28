from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from django.template import loader
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Ticket, ReviewRating
from profiles.models import Profile
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model 


from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from django.contrib import messages

##

from crispy_forms.utils import render_crispy_form
from django.http import HttpResponse
from django.contrib.auth.models import User
##


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'feed.html' # 'ticket_list' replaced by 'feed'
    login_url = 'login'



class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'
    login_url = 'login'


# class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    fields = ('title', 'description', 'image')
    template_name = 'ticket_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == Profile.objects.get(user=self.request.user)


class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    template_name = 'ticket_delete.html'
    success_url = reverse_lazy('feed')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == Profile.objects.get(user=self.request.user)



class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'ticket_new.html'
    fields = ('title', 'description', 'image', )
    login_url = 'login'

    def form_valid(self, form):
        # form.instance.author = self.request.user
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


@login_required
def submit_review(request, pk):
    """review function"""
    url = request.META.get('HTTP_REFERER') # 'url' so that the user redirect to 'ticket detail' page
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, ticket__id=pk)
            form = ReviewForm(request.POST, instance=reviews) # 'instance=reviews' is passed here to update review, not to create a new one
            form.save()
            messages.success(request, 'Merci. Votre critique a bien été actualisée!')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST) # form corresponds to a brand new review
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ticket_id = pk
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Merci. Votre critique a bien été envoyée!')
                return redirect(url)


@login_required
def tickets_of_following_profiles(request):
    """view for user dashboard"""
    # get logged-in user profile
    profile = Profile.objects.get(user=request.user)
    # check who's being followed
    users = [user for user in profile.following.all()]
    # initial value for variables
    tickets = []
    qs= None
    # get tickets of people we are following
    for dude in users:
        p = Profile.objects.get(user=dude)
        p_tickets = p.ticket_set.all()
        tickets.append(p_tickets)
    # get our own tickets
    my_tickets = profile.profiles_tickets()
    tickets.append(my_tickets)
    # sort and chain querysets and unpack the tickets list
    if len(tickets)>0:
        qs = sorted(chain(*tickets), reverse=True, key=lambda obj: obj.created)
    # get all users
    all_users = get_user_model().objects.values()
    context= {'profile':profile, 'tickets': qs, 'allusers': all_users}
    return render(request, 'tickets/main.html', context)


@login_required
def my_feed_tickets_of_following_profiles(request):
    """view for user dashboard"""
    # get logged-in user profile
    profile = Profile.objects.get(user=request.user)
    # check who's being followed
    users = [user for user in profile.following.all()]
    # initial value for variables
    tickets = []
    qs= None
    # get tickets of people we are following
    for dude in users:
        p = Profile.objects.get(user=dude)
        p_tickets = p.ticket_set.all()
        tickets.append(p_tickets)
    # get our own tickets
    my_tickets = profile.profiles_tickets()
    tickets.append(my_tickets)
    # sort and chain querysets and unpack the tickets list
    if len(tickets)>0:
        qs = sorted(chain(*tickets), reverse=True, key=lambda obj: obj.created)
    # get all users
    all_users = get_user_model().objects.values()
    context= {'profile':profile, 'tickets': qs, 'allusers': all_users}
    return render(request, 'tickets/myfeed.html', context)


@login_required
def others_feed_tickets_of_following_profiles(request):
    """view for other users feed"""
    # get logged-in user profile
    profile = Profile.objects.get(user=request.user)
    # check who's being followed
    users = [user for user in profile.following.all()]
    # initial value for variables
    tickets = []
    qs= None
    # get tickets of people we are following
    for dude in users:
        p = Profile.objects.get(user=dude)
        p_tickets = p.ticket_set.all()
        tickets.append(p_tickets)
    # get our own tickets
    my_tickets = profile.profiles_tickets()
    tickets.append(my_tickets)
    # sort and chain querysets and unpack the tickets list
    if len(tickets)>0:
        qs = sorted(chain(*tickets), reverse=True, key=lambda obj: obj.created)
    # get all users
    all_users = get_user_model().objects.values()
    context= {'profile':profile, 'tickets': qs, 'allusers': all_users}
    return render(request, 'tickets/othersfeed.html', context)


@login_required
def user_search(request):
    """search bar"""
    if request.method == "POST":
        searched = request.POST['searched']
        users = get_user_model().objects.filter(username__contains=searched).exclude(username=request.user) # Good good
        return render(request, 'tickets/user_search.html', {'searched':searched, 'users':users})
    else:
        return render(request, 'tickets/user_search.html', {} )
