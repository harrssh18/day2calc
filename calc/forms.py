from django import forms 

class LCMForm(forms.Form):
	num1 = forms.IntegerField(label="LCM OF",widget=forms.TextInput(attrs={'placeholder': 'Number 1'}))
	num2 = forms.IntegerField(label="AND",widget=forms.TextInput(attrs={'placeholder': 'Number 2'}))
