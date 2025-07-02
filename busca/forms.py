from django import forms

class BuscaForm(forms.Form):
    nome_produto = forms.CharField(
        label='Nome ou Marca do Produto',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    arquivo_lista = forms.FileField(
        label='Upload de lista de produtos (.txt ou .xlsx)',
        required=False
    )
