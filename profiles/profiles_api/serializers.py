from rest_framework import serializers

class HomeSerializer(serializers.Serializer):
    """ Serializes a name field for testing out our ApiView"""
    name = serializers.CharField(max_length=20)