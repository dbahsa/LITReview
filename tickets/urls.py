from django.urls import path

from .views import (
    TicketListView,
    TicketUpdateView,
    TicketDetailView, 
    TicketDeleteView,
    TicketCreateView,
    submit_review,
    # create_review,
    # tickets_of_following_profiles,
    
)

# app_name = 'tickets'

urlpatterns = [
    path('<int:pk>/edit/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('new/', TicketCreateView.as_view(), name='ticket_new'),
    path('', TicketListView.as_view(), name='ticket_list'),

    path('submit_review/<int:pk>/', submit_review, name='submit_review'),
    # replace ticket_id by pk
    
    # path('review_new/', create_review, name='review_new'), # OK
    # path('<int:pk>/review_edit/', create_review, name='review_edit'),

    # path('review_new/', ReviewCreateView.as_view(), name='review_new'),

    ## path for tickets and profiles both combined,
    # path('', tickets_of_following_profiles, name="tickets-follow-view"),
]
