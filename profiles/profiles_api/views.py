from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .serializers import HomeSerializer, UserProfileSerializer, StudentProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile


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

class UserProfileViewset(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class HomeApiViewset(viewsets.ViewSet):
    """Test API viewsets"""

    serializer_class = HomeSerializer

    def list(self, request):
        """Return a message"""

        a_viewset = [
            'uses actions',
            'maps automatically',
            'provides more functionality'
        ]

        return Response({
            'message': 'Testing viewsets',
            'a_viewset': a_viewset
        })

    def create(self, request):
        """Creating a new message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({
                'message': message
            })

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handles querying messages by id"""

        return Response({
            'http_method': 'GET'
        })

    def update(self, request, pk=None):
        """Handles updating messages with id"""
        return Response({
            'http_method': 'PUT'
        })

    def patch(self, request, pk=None):
        """ Handles updating part of an object"""
        return Response({
            'http_method': 'PATCH'
        })

    def destroy(self, request, pk=None):
        """Handles remove object """
        return Response({
            'http_method': 'DELETE'
        })

class StudentProfileViewset(viewsets.ModelViewSet):
    """ Handles updating and creating student profiles"""

    serializer_class = StudentProfileSerializer

    queryset = UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)








