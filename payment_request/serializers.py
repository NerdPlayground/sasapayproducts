from rest_framework import serializers

class NumberRequestPaymentSerializer(serializers.Serializer):
    MerchantCode= serializers.IntegerField()
    PhoneNumber= serializers.IntegerField()
    TransactionDesc= serializers.CharField()
    AccountReference= serializers.CharField()
    Currency= serializers.CharField()
    Amount= serializers.IntegerField()
    CallBackURL= serializers.CharField()

class AliasNumberRequestPaymentSerializer(serializers.Serializer):
    MerchantCode= serializers.CharField()
    AliasNumber= serializers.CharField()
    TransactionType= serializers.CharField()
    transaction_ref= serializers.CharField()
    TransactionDesc= serializers.CharField()
    AccountReference= serializers.CharField()
    Currency= serializers.CharField()
    Amount= serializers.IntegerField()
    CallBackURL= serializers.CharField()