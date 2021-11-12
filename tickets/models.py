from typing import Any
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse



class Ticket(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('ticket_detail', args=[str(self.id)])


# Ticket Review
class TicketReview(models.Model):
    
    RATINGS = (
            ('0', '- 0'),
            ('1', '- 1'),
            ('2', '- 2'),
            ('3', '- 3'),
            ('4', '- 4'),
            ('5', '- 5'),
        )
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments',)
    headline = models.CharField(max_length=128, default=None, blank=True)
    rating = models.CharField(max_length=100 , choices=RATINGS, null=True)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.rating

    def get_absolute_url(self):
        return reverse('ticket_list')


# class UserFollows(models.Model):
#     # Your UserFollows model definition goes here

#     class Meta:
#         # ensures we don't get multiple UserFollows instances
#         # for unique user-user_followed pairs
#         unique_together = ('user', 'followed_user', )
