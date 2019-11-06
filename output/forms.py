from django import forms

class OutputForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea)