from typing import Any
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from profiles.models import Profile



class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('ticket_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-created']


################ CURRENTLY ######################

class ReviewRating(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=128, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['ticket','user'],  name="unique_comments")
    #     ]
    ## or use this so that there can be only one ticket/user
        # unique_together = ('ticket', 'user', ) ## deprecated!!!
