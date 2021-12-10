from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from django.db.models import Q

from .models import Ticket, ReviewRating
from profiles.models import Profile

from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from django.contrib import messages

##

from crispy_forms.utils import render_crispy_form
from django.http import HttpResponse

##


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket_list.html'
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


# replace ticket_id by pk
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
    return render(request, 'tickets/main.html', {'tickets': tickets})



# def search(request):
#     if 'keyword' in request.GET:
#         keyword = request.GET['keyword']
#         if keyword:
#             tickets = ticket.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(ticket_name__icontains=keyword))
#             ticket_count = tickets.count()
#     context = {
#         'tickets': tickets,
#         'ticket_count': ticket_count,
#     }
#     return render(request, 'store/store.html', context)
