from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from rest_framework.response import Response

from .models import Device

from . import main
from .weatherinfo import get_weatherinfo


class WeatherInfoViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        light_id = 0
        return Response(get_weatherinfo())
