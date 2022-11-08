from django import forms

class ContactForms(forms.Form):
    
    name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'size':29}), required=True)

    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'size':29}), required=True)
    
    content = forms.CharField(label='Contenido', widget=forms.Textarea(attrs={'rows':8, 'cols':30, 'spellcheck':False}))