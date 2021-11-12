from django import forms

from .models import TicketReview

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=TicketReview.RATINGS, widget=forms.RadioSelect)

    class Meta:
        model = TicketReview
        # fields = "__all__"
        fields = ('ticket', 'rating', 'headline', 'body')
