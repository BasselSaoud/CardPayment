from django import forms

class PaymentForm(forms.Form):
    api_key = forms.CharField(label='API Key', max_length=300)
    transaction_amount = forms.CharField(label='Transaction Amount', max_length=100)
    integration_id = forms.CharField(label='Payment Integration ID', max_length=100)
    iframe_id = forms.CharField(label='iFrame ID', max_length=100)