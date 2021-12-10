from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    following = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='following', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def profiles_tickets(self):
        return self.ticket_set.all()

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-created',)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['user','following'],  name="unique_comments")
    #     ]
    ## or use so that there can be only one ticket/user
        # unique_together = ('user', 'following', ) ## deprecated!!!
