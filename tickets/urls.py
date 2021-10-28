from django.urls import path

from .views import (
    TicketListView,
    TicketUpdateView,
    TicketDetailView, 
    TicketDeleteView,
    TicketCreateView,
)


urlpatterns = [
    path('<int:pk>/edit/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('new/', TicketCreateView.as_view(), name='ticket_new'),
    path('', TicketListView.as_view(), name='ticket_list'),
]
