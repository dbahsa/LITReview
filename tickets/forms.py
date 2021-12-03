from django import forms
# from django.urls.base import translate_url

from .models import ReviewRating

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Row, Column
# from crispy_forms.bootstrap import InlineRadios, FormActions







################ DEV BEFORE DEC 2 ###################

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']







################ DEV BEFORE DEC 2 ###################

# class RateForm(forms.ModelForm):
#     rate = forms.ChoiceField(choices=Review.RATINGS, widget=forms.RadioSelect, required=True)

#     class Meta:
#         model = Review
#         # fields = "__all__"
#         fields = ('ticket', 'rating', 'headline', 'comment')

    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.forms_method = 'post'
#         # self.helper.attrs = {
#         #     'novalidate' : ''
#         # }

#         self.helper.layout = Layout(
#             Row(Column('ticket'), Column('headline'),),
#             InlineRadios('rate'),
#             'comment',
#             FormActions(
#                 Submit('save_review', 'Envoyer', css_class='btn btn-success'),
#                 Submit('cancel_review', 'Annuler', css_class='ml-4 btn btn-danger')
#             )
#         )
