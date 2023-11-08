from django import forms
from .models import NewOrder

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderCreate(forms.ModelForm):
    class Meta:
        model = NewOrder
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия',
                  'email': 'Эл.почта', 'phone': 'Тел.', 'address': 'Адрес'}

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input_text long_input',
                                                 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'input_text long_input',
                                                'placeholder': 'Фамилия'}),

            'email': forms.EmailInput(attrs={'placeholder': 'Фамилия'}),
            'phone': forms.TextInput(attrs={'class': 'input_text long_input',
                                            'placeholder': '+7...'}),
            'address': forms.TextInput(attrs={'class': 'input_text long_input',
                                              'placeholder': 'Адрес доставки'}),

        }
