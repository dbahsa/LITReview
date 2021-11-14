from django.urls import path

from .views import (
    TicketListView,
    TicketUpdateView,
    TicketDetailView, 
    TicketDeleteView,
    TicketCreateView,
    create_review
    
)



urlpatterns = [
    path('<int:pk>/edit/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('new/', TicketCreateView.as_view(), name='ticket_new'),
    path('', TicketListView.as_view(), name='ticket_list'),

    # path('<int:pk>/edit/', TicketUpdateView.as_view(), name='review_edit'),
    # path('<int:pk>/', TicketDetailView.as_view(), name='review_detail'),
    # path('<int:pk>/delete/', TicketDeleteView.as_view(), name='review_delete'),
    # path('review_new/', create_review, name='review_new'), # OK
    path('review_new/', create_review, name='review_new'),
    # path('', TicketListView.as_view(), name='review_list'),
]
