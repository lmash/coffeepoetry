from django import forms

from .models import Cafe, Image


class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        exclude = ["rating", "contributor"]

        widgets = {
            'name': forms.TextInput(attrs={'size': 50, }),
            'description': forms.Textarea(attrs={'rows': 6, 'cols': 120, }),
            'location': forms.TextInput(attrs={'size': 50, }),
            # 'url': forms.TextInput(attrs={'size': 70, 'placeholder': 'auctions/images/xxxxx.jpg'}),
        }


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Image
        fields = ('name',)
