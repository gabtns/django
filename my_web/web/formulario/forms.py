from django import forms

class formularios(forms.Form):
    nombre = forms.CharField(required=True,
                             widget= forms.TextInput(attrs={'class': 'formulate',
                                                            'placeholder':'Nombre'}),
                            error_messages={'required':" Ingrese su nombre " })

    empresa = forms.CharField(required=True,
                              widget= forms.TextInput(attrs={'class': 'formulate',
                                                             'placeholder':'Empresa'}),
                            error_messages={'required':" Ingrese su empresa " })

    email = forms.EmailField(required=True,
                            widget= forms.EmailInput(attrs={'class': 'formulate',
                                                            'placeholder':'Mail'}),
                            error_messages={'required':" Ingrese su empresa "})

    texto = forms.CharField(required=True,
                            widget= forms.TextInput(attrs={'class': 'formulate',
                                                           'placeholder':'Mensaje'}),
                            error_messages={'required':" Ingrese su consulta " })