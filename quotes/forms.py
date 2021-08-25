from django import forms
from.models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        exclude  = ['author', 'likes']
        widgets = {
                'quote': forms.Textarea(attrs={
                    'class': 'form-control',
                    'max-length': '255',
                    'rows': '6',
                    'cols': '40'}),
                }

class UpdateQuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        exclude  = ['author', 'likes']
        widgets = {
                'quote': forms.Textarea(attrs={
                 'class': 'form-control',
                 'max-length': '255',
                 'rows': '6',
                 'cols': '40'}),
                }

class DeleteQuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        exclude  = ['author', 'likes']
