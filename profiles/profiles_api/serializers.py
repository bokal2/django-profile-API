from rest_framework import serializers
from .models import UserProfile

class HomeSerializer(serializers.Serializer):
    """ Serializes a name field for testing out our ApiView"""
    name = serializers.CharField(max_length=20)

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializers a user profile object"""

    class Meta:
        model = UserProfile

        fields = ['id', 'email', 'password', 'name']

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new User"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

class StudentProfileSerializer(serializers.ModelSerializer):
    """ student profile Serializer """

    class Meta:
        model = UserProfile

        fields = ['id', 'email', 'password', 'name']

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

        def create(self, validated_data):
            """Create and return a new User"""
            user = UserProfile.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password']
            )

            return user

