from django import forms


class LivroForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields =[
            'titulo',
            'autor',
            'lancamento',
            'genero',
            'descricao'
        ]

