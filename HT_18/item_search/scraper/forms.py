from django import forms
from django.core.validators import RegexValidator


class GetProductIdsForm(forms.Form):
    ids_raw_data = forms.CharField(
        label='Введіть ID продуктів, розділені комою',
        max_length=5000,
        validators=[
            RegexValidator(
                # regex=r'^[a-zA-Z\d,]+$',
                # code='invalid_input',
            ),
        ]
    )