from django.forms import ModelForm

from mylotto.models import GuessNumbers


class PostForm(ModelForm):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text', 'num_lotto')