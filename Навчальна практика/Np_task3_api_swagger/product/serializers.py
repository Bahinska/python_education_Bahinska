from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer of Product model
    """
    class Meta:
        """
         Shortcut for info about serializable model
         """
        model = Product
        fields = '__all__'

    def validate(self, data):
        """
        function for validating correct date data
        """
        if data["created_at"] > data["updated_at"]:
            raise serializers.ValidationError("created date can't be less than updated")
        return data

