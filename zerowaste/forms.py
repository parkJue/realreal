from django import forms
from .models import Shop, Oreview, Nkreview, Ask

class AskForm(forms.ModelForm):
    class Meta:
        model = Ask
        fields = "__all__"

# FIXME: 지워주세요.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Oreview
        # fields = '__all__'
        exclude = ('article', 'user',)


class OreviewForm(forms.ModelForm):
    class Meta:
        model = Oreview
        fields = ['content']
