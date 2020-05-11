from django import forms


class pic_form(forms.Form):
    name=forms.CharField(required=True)
    img=forms.ImageField()