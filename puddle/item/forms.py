from django import forms

from .models import Item, Note

INPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
    
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASS}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASS}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASS}),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image','is_sold')
    
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASS}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASS}),
        }
        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'subject', 'description', 'file', 'is_free', 'price']
        widgets = {
            'description': forms.Textarea(attrs={"class": INPUT_CLASS}),
            'file': forms.FileInput(attrs={'class': INPUT_CLASS}),
            'is_free': forms.CheckboxInput(attrs={'class': 'form-checkbox h-5 w-5 text-gray-600'}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASS}),
        }
    def clean(self):
        cleaned_data = super().clean()
        is_free = cleaned_data.get("is_free")
        price = cleaned_data.get("price")

        if not is_free and price is None:
            raise forms.ValidationError("Price is required if the note is not free.")

        return cleaned_data