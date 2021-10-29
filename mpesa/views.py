from decouple import config
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework_simplejwt import authentication
from PIL import Image
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from accounts.models import UserAccount
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
import requests
from requests.auth import HTTPBasicAuth
import json
from django.views.decorators.csrf import csrf_exempt
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from .models import MpesaPayment

# Create your views here.


def getAccessToken(request):
    consumer_key = config('CONS_KEY')
    consumer_secret = config('CONS_SECRET')
    api_URL = config('API_URL')

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)


@api_view(["POST"])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def lipa_na_mpesa_online(request):
    data = request.data
    mobile = data["mobile"]
    print(mobile)
    amount = data["amount"]
    category = data["category"]
    poultry_id = data["id"]
    access_token = MpesaAccessToken.validated_mpesa_access_token
    stk_url = config('STK_URL')
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": mobile,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": mobile,  # replace with your phone number to get stk push
        "CallBackURL": config('CallBackURL'),  # your callback url
        "AccountReference": "E-KUKU Online MarketPlace",
        "TransactionDesc": "Testing stk push"
    }
    try:
        response = requests.post(stk_url, json=request, headers=headers)
        return HttpResponse('success')
    except:
        return HttpResponse('Failed')


@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://98e0-41-89-141-2.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://98e0-41-89-141-2.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):
    pass


@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body = request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
