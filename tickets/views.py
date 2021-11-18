from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

# from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Ticket #, Review

from django.shortcuts import render
from .forms import RateForm

##
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from django.http import HttpResponse
import json

from django.db.models import CharField, Value

##

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket_list.html'
    login_url = 'login'



class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'
    login_url = 'login'


class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    fields = ('title', 'description', 'image')
    template_name = 'ticket_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    template_name = 'ticket_delete.html'
    success_url = reverse_lazy('ticket_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'ticket_new.html'
    fields = ('title', 'description', 'image', )
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


        
def create_review(request):
    form = RateForm()
    
    if request.method == 'POST':
        form = RateForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        return render(request, 'ticket_list.html')

    context = {'form': form}
    return render(request, 'review_new.html', context)



    ## functional codes
    # form = RateForm()
    # if request.method == 'POST':
    #     form = RateForm(request.POST)
    #     form.instance.user = request.user
    #     if form.is_valid():
    #         form.save()
    #     return render(request, 'ticket_list.html')
    # context = {'form': form}
    # return render(request, 'review_new.html', context)
    

    ## from help doc
    # reviews = get_users_viewable_reviews(request.user)
    # # returns queryset of reviews
    # reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    # tickets = get_users_viewable_tickets(request.user)
    # # returns queryset of tickets
    # tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    # # combine and sort the two types of posts
    # posts = sorted(
    #     chain(reviews, tickets),
    #     key=lambda post: post.time_created,
    #     reverse=True
    # )
    # return render(request, 'feed.html', context={'posts': posts})