from rest_framework import serializers
import re
from product.models import Product, UserData
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


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


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        """
         Shortcut for info about serializable model
         """
        model = UserData
        fields = ["id", "email", "first_name", "last_name", "password", "role"]

    def validate(self, data):
        """
        function for validating correct user data
        """
        dict_of_errors = {}

        pass_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        if not re.match(pass_regex, data['password']):
            dict_of_errors['password'] = "invalid password"

        email_regex = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
        if not re.match(email_regex, data['email']):
            dict_of_errors['email'] = "invalid email"

        first_regex = '[A-Z][A-Za-z]{2,25}$'
        if not re.match(first_regex, data['first_name']):
            dict_of_errors['first_name'] = "invalid first_name"

        last_regex = '[A-Z][A-Za-z]{2,25}$'
        if not re.match(last_regex, data['last_name']):
            dict_of_errors['last_name'] = "invalid last_name"

        if len(dict_of_errors) != 0:
            raise serializers.ValidationError(dict_of_errors)
        return data

    def create(self, validated_data):
        """
         function for creating user in database
        """
        user = UserData.objects.create(email=validated_data['email'],
                                       first_name=validated_data['first_name'],
                                       last_name=validated_data['last_name'],
                                       role=validated_data['role'])
                                    #is_admin=validated_data['is_admin'])
        user.set_password(validated_data['password'])
        user.save()
        return user
