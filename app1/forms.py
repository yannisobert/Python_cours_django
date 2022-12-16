from django import forms
from app1.models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"
