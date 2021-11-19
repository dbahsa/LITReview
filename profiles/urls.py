from django.urls import path

from .views import ProfileListView, ProfileDetailView


app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list-view'),
    path('<pk>/', ProfileDetailView.as_view(), name='profile-detail-view'),
]
