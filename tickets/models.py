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


class Comment(models.Model):
    
    choices = (
            ('0', '- 0'),
            ('0', '- 0'),
            ('0', '- 0'),
            ('0', '- 0'),
            ('0', '- 0'),
            ('0', '- 0'),
        )
    
    ticket = models.ForeignKey(
        Ticket, 
        on_delete=models.CASCADE,
        related_name='comments',
    )
    # ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    # rating = models.PositiveSmallIntegerField(
    #     # validates that rating must be between 0 and 5
    #     validators=[MinValueValidator(0), MaxValueValidator(5)])

    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    )
    
    
    # headline = models.CharField(max_length=128)
    # body = models.CharField(max_length=8192, blank=True)
    # user = models.ForeignKey(
    #     to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # time_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment


    def get_absolute_url(self):
        return reverse('ticket_list')


# class UserFollows(models.Model):
#     # Your UserFollows model definition goes here

#     class Meta:
#         # ensures we don't get multiple UserFollows instances
#         # for unique user-user_followed pairs
#         unique_together = ('user', 'followed_user', )
