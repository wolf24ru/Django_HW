from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField()

    class Meta:
        model = Product
        fields = "__all__"


class ProductPositionSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ["address", "positions"]

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.create(stock=stock,
                                        product=position['product'],
                                        quantity=position['quantity'],
                                        price=position['price'])
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        for position in positions:
            StockProduct.objects.update_or_create(stock=instance.pk, product=position['product'], defaults={
                'stock': stock,
                'product': position['product'],
                'quantity': position['quantity'],
                'price': position['price']
            })
        return stock


