from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingView(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
