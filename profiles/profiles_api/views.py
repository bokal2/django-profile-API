from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HomeSerializer

class HomeApiView(APIView):
    """ Testing API View """

    serializer_class = HomeSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features"""

        an_apiview = [
            'List all the features for rest-framework',
            'provides flexibility fo business logic'
        ]

        return Response({
            "message": "succes",
            "an_apiview": an_apiview
        })

    def post(self, request):
        """ Serializer with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            name_length = len(name)

            return Response({
                'message': message,
                'name': name_length
            })

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """Handles partial update of the object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handles deleting of objects"""
        return Response({'method': 'DELETE'})





