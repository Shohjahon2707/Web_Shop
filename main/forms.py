from django import forms

class CategoryFilterForm(forms.Form):
    category = forms.ChoiceField(required=False, label='Категория')

    def __init__(self, *args, **kwargs):
        categories = kwargs.pop('categories', [])
        super().__init__(*args, **kwargs)
        choices = [('', 'Все товары')] + [(c.name, c.name) for c in categories]
        self.fields['category'].choices = choices
