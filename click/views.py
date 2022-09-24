import os

import requests
from requests.auth import HTTPBasicAuth

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from backend.models import Payment
from . import utils
from . import Services


BROKER_API_URL = 'http://91.204.239.44/broker-api/send'


def send_code(phone_number, code):
    basic = HTTPBasicAuth(os.getenv('BROKER_API_LOGIN'),
                          os.getenv('BROKER_API_PASSWORD'))
    data = {
        "messages": [
            {
                "recipient": phone_number.removeprefix('+'),
                "message-id": "abc000000001",
                "sms": {
                    "originator": "3700",
                    "content": {
                        "text": f"Beruniy avlodlari\nKod: {code}"
                    }
                }
            }
        ]
    }

    requests.post(BROKER_API_URL, json=data, auth=basic)


@csrf_exempt
def prepare(request):
    return utils.prepare(request)


@csrf_exempt
def complete(request):
    payment_id = request.POST['merchant_trans_id']
    payment = Payment.objects.get(id=payment_id)
    if payment.individual_request:
        payment.individual_request.paid = True
        payment.individual_request.save()

    if payment.entity_request:
        payment.entity_request.paid = True
        payment.entity_request.save()

    if payment.user:
        phone_number = payment.user.phone_number
        send_code(phone_number, payment.user.key)

    return utils.complete(request)


@csrf_exempt
def service(request, service_type):
    service = Services(request.POST, service_type)
    return JsonResponse(service.api())
