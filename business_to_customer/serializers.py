from rest_framework import serializers

class B2CPaymentsSerializer(serializers.Serializer):
    MerchantCode= serializers.IntegerField()
    MerchantTransactionReference= serializers.CharField()
    Currency= serializers.CharField()
    Amount= serializers.IntegerField()
    ReceiverNumber= serializers.CharField()
    Channel= serializers.IntegerField()
    CallBackURL= serializers.CharField()
    Reason= serializers.CharField()