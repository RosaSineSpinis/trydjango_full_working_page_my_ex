from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    '''this title here shows that we can overwrite it,
     not sure which is first title ot meta title'''
    title       = forms.CharField(
                        label='',
                        widget=forms.TextInput(
                            attrs={
                                "placeholder": "example title"}),
                                required=True) #True is default

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "example title",
                "class": "new-class-name two",
                "id": "my_id_name",
                "rows": 20,
                "col": 120
            }))
    price = forms.DecimalField(
        initial=20.00
    )
    '''only this meta class is enough for ModelForm, I think this method above override it'''
    class Meta:
        model = Product
        fields = [
                'title',
                'description',
                'price'
        ]

    def clean_title(self, *args, **kwargs): #title is name of attr
        title = self.cleaned_data.get("title")
        if "abc" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

'''we are trying to obatin model.form from class below - we want to look it as ProductForm above'''
class RawProductForm(forms.Form):
    title       = forms.CharField(
                        label='',
                        widget=forms.TextInput(
                            attrs={
                                "placeholder": "example title"}),
                                required=True) #True is default
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "example title",
                                "class": "new-class-name two",
                                "id": "my_id_name",
                                "rows": 20,
                                "col": 120
                            }))
    price       = forms.DecimalField(
                        initial=20.00
                        )
