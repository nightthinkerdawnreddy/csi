from django import forms
class contactformemail(forms.Form):
    name=forms.CharField(required=True)
    fromemail=forms.EmailField(required=True)
    Subject=forms.CharField(required=True)
    Message=forms.CharField(widget=forms.Textarea, required=True)
