from django import forms

class formularios(forms.Form):
    nombre = forms.CharField(required=True,
                             widget= forms.TextInput(attrs={'class': 'formulate',
                                                            'placeholder':'Nombre'}))

    empresa = forms.CharField(required=True,
                              widget= forms.TextInput(attrs={'class': 'formulate',
                                                             'placeholder':'Empresa'}))

    email = forms.EmailField(required=True,
                            widget= forms.EmailInput(attrs={'class': 'formulate',
                                                            'placeholder':'Mail'}))

    texto = forms.CharField(required=True,
                            widget= forms.TextInput(attrs={'class': 'formulate',
                                                           'placeholder':'Mensaje'}))