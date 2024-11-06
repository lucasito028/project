from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name','phone',
            'email','description','category',
            'picture',

        )
        # Método clean é usada quando precisamos validar campos no formulários,
        # este método é chamado antes de salvar os dados na base de dados

        def clean(self):
            cleaned_data = self.cleaned_data
            self.add_error(
                'first_name',
                ValidationError(
                    'Mensagem de erro',
                    code='invalid'
                )
            )
            self.add_error(
                'first_name',
                ValidationError(
                    'Mensagem de erro 2',
                    code='invalid'
                )
            )
            return super().clean()