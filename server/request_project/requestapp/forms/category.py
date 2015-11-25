from django import forms
from requestapp.models import Category


class FormCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
