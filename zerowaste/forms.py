from django import forms
from .models import Shop, Oreview, Nkreview, Ask

from django import forms

from .models import Ask

class ArticleForm(forms.ModelForm):
    email = forms.CharField(
                max_length=100,
                label='이메일 주소',
                widget=forms.TextInput(
                        attrs={
                            'class': 'my-input',
                            'placeholder': '회신 받고 싶은 이메일 주소를 입력해 주세요.'
                        }
                    )
            )

    content = forms.CharField(
                label='내용',
                widget=forms.Textarea(
                        attrs={
                            'row': 5,
                            'col': 50,
                            'placeholder': '문의사항 혹은 건의사항을 자유롭게 작성해 주세요.',
                            'style': 'height:150px'
                        }
                    )
            )
    class Meta:
        model = Ask
        fields = ['email', 'content']

# FIXME: 지워주세요.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Oreview
        # fields = '__all__'
        exclude = ('article', 'user',)


class OreviewForm(forms.ModelForm):
    content = forms.CharField(
                label='리뷰',
                widget=forms.Textarea(
                        attrs={
                            'row': 5,
                            'col': 50,
                            'placeholder': '매장 방문 후기를 자유롭게 작성해 주세요.',
                            'style': 'height:100px'
                        }
                    )
            )
    class Meta:
        model = Oreview
        fields = ['content']
