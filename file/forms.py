from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
      class Meta:
          model = Document
          fields = ['title']
          widgets = {
              'title': forms.TextInput(attrs={
                  'placeholder': 'Fayl nomi...',
                  'class': 'form-control'
              }),
          }

class CreateDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
