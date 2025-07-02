from django import forms

class BuscaForm(forms.Form):
    nome_produto = forms.CharField(
        label='Nome ou Marca do Produto',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
