from rest_framework.views import APIView
from rest_framework.response import Response

class HomeApiView(APIView):
    """ Testing API View """

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





