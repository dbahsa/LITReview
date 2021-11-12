from django import forms

from .models import TicketReview

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.bootstrap import InlineRadios, FormActions


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=TicketReview.RATINGS, widget=forms.RadioSelect)

    class Meta:
        model = TicketReview
        # fields = "__all__"
        fields = ('ticket', 'rating', 'headline', 'body')

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.forms_method = 'post'
        # self.helper.attrs = {
        #     'novalidate' : ''
        # }

        self.helper.layout = Layout(
            Row(Column('ticket'), Column('headline'),),
            InlineRadios('rating'),
            'body',
            FormActions(
                Submit('save_review', 'Envoyer', css_class='btn btn-success'),
                Submit('cancel', 'Annuler', css_class='ml-4 btn btn-danger')
            )
        )
