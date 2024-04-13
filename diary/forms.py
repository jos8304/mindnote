from django import forms

class PageForm(forms.Form):
    title = forms.CharField(max_length=100, label="Title")
    content = forms.CharField(label="content", widget=forms.Textarea)
    feeling = forms.CharField(max_length=80, label="feeling")
    score = forms.IntegerField(label="score")
    dt_created = forms.DateField(label="Date")
