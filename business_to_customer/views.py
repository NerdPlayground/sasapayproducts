import json
import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from authentication.authentication import get_client_token
from business_to_customer.serializers import B2CPaymentsSerializer

class B2CPaymentsAPIView(GenericAPIView):
    serializer_class= B2CPaymentsSerializer

    def post(self,request):
        data= request.data
        serializer= B2CPaymentsSerializer(data=data)
        if serializer.is_valid():
            merchant_code= data.get("MerchantCode")
            merchant_transaction_reference= data.get("MerchantTransactionReference")
            currency= data.get("Currency")
            amount= data.get("Amount")
            receiver_number= data.get("ReceiverNumber")
            channel= data.get("Channel")
            call_back_url= data.get("CallBackURL")
            reason= data.get("Reason")

            client_token= get_client_token()
            headers= {
                "Authorization": "Bearer %s" %client_token["access_token"]
            }

            payload={
                "MerchantCode":merchant_code,
                "MerchantTransactionReference":merchant_transaction_reference,
                "Currency":currency,
                "Amount":amount,
                "ReceiverNumber":receiver_number,
                "Channel":channel,
                "CallBackURL":call_back_url,
                "Reason":reason,
            }
            
            response= requests.post(
                "%s" %settings.PAYMENTS_B2C,
                json=payload,
                headers=headers
            )

            if response.status_code == 200:
                response= json.loads(response.text)
                return Response(
                    response,
                    status= status.HTTP_200_OK
                )
            else:
                response= json.loads(response.text)
                return Response(
                    response,
                    status= status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )