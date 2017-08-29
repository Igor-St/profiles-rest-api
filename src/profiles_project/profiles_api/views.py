from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.views import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """REturns a list of APIView features."""

        an_apiview = [
            'Uses http method ad function (get, posst, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
