from django import forms
from requestapp.models import Item, Category


class FormItem(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects.get_actives())

    class Meta:
        model = Item
        fields = "__all__"
