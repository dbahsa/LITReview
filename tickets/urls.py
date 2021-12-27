from django.urls import path

from .views import (
    TicketListView,
    TicketUpdateView,
    TicketDetailView, 
    TicketDeleteView,
    TicketCreateView,
    submit_review,
    tickets_of_following_profiles,
    user_search,
    
)

# app_name = 'tickets'

urlpatterns = [
    path('<int:pk>/edit/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('new/', TicketCreateView.as_view(), name='ticket_new'),
    path('', TicketListView.as_view(), name='feed'), # 'ticket_list' replaced by 'feed'
    path('submit_review/<int:pk>/', submit_review, name='submit_review'),
    path('account/', tickets_of_following_profiles, name='tickets-follow-view'),
    path('user_search/', user_search, name='user-search'),

]
