import json
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from authentication.authentication import get_client_token
from payment_request.serializers import NumberRequestPaymentSerializer

class NumberRequestPaymentAPIView(GenericAPIView):
    def post(self,request):
        data= request.data
        serializer= NumberRequestPaymentSerializer(data=data)
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
                data=payload,
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