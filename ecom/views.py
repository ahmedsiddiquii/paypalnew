from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
import uuid
from django.contrib import messages

# Create your views here.


def home(request):
    host = request.get_host()
    paypal_dict1 = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '40.00',
        'item_name': 'Men\'s T-shirts',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-return")}',
        'cancel_url': f'http://{host}{reverse("paypal-cancel")}',
    }
    form1 = PayPalPaymentsForm(initial=paypal_dict1)
    paypal_dict2 = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '40.00',
        'item_name': 'Woman\'s T-shirts:',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-return")}',
        'cancel_url': f'http://{host}{reverse("paypal-cancel")}',
    }
    form2 = PayPalPaymentsForm(initial=paypal_dict2)
    paypal_dict3 = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '60.00',
        'item_name': 'Men\'s Sweatpants',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-return")}',
        'cancel_url': f'http://{host}{reverse("paypal-cancel")}',
    }
    form3 = PayPalPaymentsForm(initial=paypal_dict3)
    paypal_dict4 = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '60.00',
        'item_name': 'Woman\'s Sweatpants',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-return")}',
        'cancel_url': f'http://{host}{reverse("paypal-cancel")}',
    }
    form4 = PayPalPaymentsForm(initial=paypal_dict4)
    paypal_dict5 = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '50.00',
        'item_name': 'Nike Air Force Unisex',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-return")}',
        'cancel_url': f'http://{host}{reverse("paypal-cancel")}',
    }
    form5 = PayPalPaymentsForm(initial=paypal_dict5)
    
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
        }
    return render(request, 'home.html', context)

def paypal_return(request):
    messages.success(request, 'You\'ve successfully made a payment!')
    return redirect('home')

def paypal_cancel(request):
    messages.error(request, 'Your order has been cancelled!')
    return redirect('home')
