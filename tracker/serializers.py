from rest_framework import serializers
from .models import Politician, Stock, Trade

class PoliticianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politician
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'
