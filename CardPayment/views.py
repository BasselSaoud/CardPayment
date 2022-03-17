from django.shortcuts import redirect, render
from .forms import PaymentForm
from .helpers import *
from django.http import JsonResponse

def get_payment(request): 
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            auth_token_response = get_auth_token(form.cleaned_data['api_key'])
            order_registration_response = register_order(auth_token_response['token'], False, form.cleaned_data['transaction_amount'], [])
            payment_token_response = request_payment_key(auth_token_response['token'], form.cleaned_data['transaction_amount'], 3600, order_registration_response['id'], 'EGP', form.cleaned_data['integration_id'])
            return redirect('https://accept.paymobsolutions.com/api/acceptance/iframes/%s?payment_token=%s' % (form.cleaned_data['iframe_id'], payment_token_response['token']))

        return JsonResponse({'error': 'invalid form'})

    else:
        form = PaymentForm()
        return render(request, 'payment.html', {'form': form})