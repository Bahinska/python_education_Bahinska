from rest_framework import serializers
from product.models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        if data["created_at"] > data["updated_at"]:
            raise serializers.ValidationError("created date can't be less than updated")
        return data

