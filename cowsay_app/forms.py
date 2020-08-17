from django import forms


class CowsayForm(forms.Form):
  text = forms.TimeField(max_length=150)