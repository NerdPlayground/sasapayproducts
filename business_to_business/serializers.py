from rest_framework import serializers

class B2BPaymentSerializer(serializers.Serializer):
    MerchantCode= serializers.IntegerField()
    MerchantTransactionReference= serializers.CharField()
    Currency= serializers.CharField()
    Amount= serializers.IntegerField()
    ReceiverMerchantCode= serializers.IntegerField()
    CallBackURL= serializers.CharField()
    Reason= serializers.CharField()
'''
{
    "MerchantCode": "595975",
    "MerchantTransactionReference": "87065",
    "Currency":"KES",
    "Amount": 1,
    "ReceiverMerchantCode": "3209",
    "CallBackURL": "https://posthere.io/4bdd-47d5-a54d",
    "Reason": "Payment of transportation fee"
}
'''