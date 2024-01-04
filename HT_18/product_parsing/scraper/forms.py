from django import forms


class AddProductsForm(forms.Form):
    id_string = forms.CharField(widget=forms.Textarea)
