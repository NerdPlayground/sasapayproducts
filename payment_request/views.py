import json
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from authentication.authentication import get_client_token
from payment_request.serializers import (
    ProcessPaymentSerializer,
    PhoneNumberRequestPaymentSerializer,
    AliasNumberRequestPaymentSerializer,
)

class PhoneNumberRequestPaymentAPIView(GenericAPIView):
    serializer_class= PhoneNumberRequestPaymentSerializer

    def post(self,request):
        data= request.data
        serializer= PhoneNumberRequestPaymentSerializer(data=data)
        if serializer.is_valid():
            account_reference= data.get("AccountReference")
            merchant_code= data.get("MerchantCode")
            phone_number= data.get("PhoneNumber")
            transaction_desc= data.get("TransactionDesc")
            currency= data.get("Currency")
            amount= data.get("Amount")
            call_back_url= data.get("CallBackURL")

            payload={
                "MerchantCode": merchant_code,
                "PhoneNumber": phone_number,
                "TransactionDesc": transaction_desc,
                "AccountReference": account_reference,
                "Currency": currency,
                "Amount": amount,
                "CallBackURL": call_back_url
            }
            client_token= get_client_token()
            headers= {
                "Authorization":"Bearer %s" %client_token["access_token"]
            }
            
            response= requests.post(
                "https://api.sasapay.me/api/v1/payments/request-payment/",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                response= json.loads(response.text)
                return Response(
                    response,
                    status=status.HTTP_200_OK
                )
            else:
                response= json.loads(response.text)
                return Response(
                    response,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class AliasNumberRequestPaymentAPIView(GenericAPIView):
    serializer_class= AliasNumberRequestPaymentSerializer

    def post(self,request):
        data= request.data
        serializer= AliasNumberRequestPaymentSerializer(data=data)
        if serializer.is_valid():
            merchant_code= data.get("MerchantCode")
            alias_number= data.get("AliasNumber")
            transaction_type= data.get("TransactionType")
            transaction_ref= data.get("transaction_ref")
            transaction_desc= data.get("TransactionDesc")
            account_reference= data.get("AccountReference")
            currency= data.get("Currency")
            amount= data.get("Amount")
            call_back_url= data.get("CallBackURL")

            client_token= get_client_token()
            headers= {
                "Authorization": "Bearer %s" %client_token["access_token"]
            }

            payload={
                "MerchantCode": merchant_code,
                "AliasNumber": alias_number,
                "TransactionType": transaction_type,
                "transaction_ref": transaction_ref,
                "TransactionDesc": transaction_desc,
                "AccountReference": account_reference,
                "Currency": currency,
                "Amount": amount,
                "CallBackURL": call_back_url,
            }

            response= requests.post(
                "https://api.sasapay.me/api/v1/payments/request-payment-by-alias/",
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                print('Success:',response)
                response= json.loads(response.text)
                return Response(
                    response,
                    status=status.HTTP_200_OK
                )
            else:
                print('Error:',response)
                response= json.loads(response.text)
                return Response(
                    response,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class ProcessPaymentAPIView(GenericAPIView):
    serializer_class= ProcessPaymentSerializer

    def post(self,request):
        data= request.data
        serializer= ProcessPaymentSerializer(data=data)
        if serializer.is_valid():
            checkout_request_id= data.get("CheckoutRequestID")
            merchant_code= data.get("MerchantCode")
            verification_code= data.get("VerificationCode")

            client_token= get_client_token()
            headers= {
                "Authorization": "Bearer %s" %client_token["access_token"]
            }

            payload={
                "CheckoutRequestID": checkout_request_id,
                "MerchantCode": merchant_code,
                "VerificationCode": verification_code
            }

            response= requests.post(
                "https://api.sasapay.me/api/v1/payments/process-payment/",
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                response= json.loads(response.text)
                return Response(
                    response,
                    status=status.HTTP_200_OK
                )
            else:
                response= json.loads(response.text)
                return Response(
                    response,
                    status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )