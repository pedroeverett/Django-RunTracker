from django import forms
import datetime

class RuntrackerForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(), initial=datetime.date.today)
    distance = forms.DecimalField(decimal_places=0, max_digits=6, widget=forms.NumberInput(attrs={'placeholder' : 'In meters'}))
    time = forms.DecimalField(decimal_places=0, max_digits=6, widget=forms.NumberInput(attrs={'placeholder' : 'In minutes'}))