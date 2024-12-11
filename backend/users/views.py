from rest_framework import generics, viewsets
from users.models import ExtendedUser, FavouritesCars, CarRequest, AuctionClicks
from users.serializers import ExtendedUserSerializer, FavouritesCarsSerializer, CarRequestSerializer, AuctionClicksSerializer


class ExtendedUserViewSet(viewsets.ModelViewSet):
    queryset = ExtendedUser.objects.all()
    serializer_class = ExtendedUserSerializer

class FavouritesCarsViewSet(viewsets.ModelViewSet):
    queryset = FavouritesCars.objects.all()
    serializer_class = FavouritesCarsSerializer

class CarRequestViewSet(viewsets.ModelViewSet):
    queryset = CarRequest.objects.all()
    serializer_class = CarRequestSerializer

class AuctionClicksViewSet(viewsets.ModelViewSet):
    queryset = AuctionClicks.objects.all()
    serializer_class = AuctionClicksSerializer


