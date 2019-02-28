from django.shortcuts import render

# rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test Api view."""

    def get(self, request, format=None):
        """Returns a list of api features."""

        an_apiview = [
          'Uses Http methods as function (get, post, patch, put, delete)',
          'It is similar to a traditional django view',
          'Gives the most control over your logic',
          'Is mapped manually to URLS'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
