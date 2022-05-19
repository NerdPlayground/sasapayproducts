from rest_framework import serializers

class NumberRequestPaymentSerializer(serializers.Serializer):
    MerchantCode= serializers.IntegerField()
    PhoneNumber= serializers.IntegerField()
    TransactionDesc= serializers.CharField()
    AccountReference= serializers.CharField()
    Currency= serializers.CharField()
    Amount= serializers.IntegerField()
    CallBackURL= serializers.CharField()