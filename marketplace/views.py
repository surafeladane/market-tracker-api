from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions
from .models import Crop, Market, PriceEntry
from .serializers import (
    CropSerializer, MarketSerializer, PriceEntrySerializer, SignupSerializer
)

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class PriceEntryViewSet(viewsets.ModelViewSet):
    queryset = PriceEntry.objects.all().order_by('-date_submitted')
    serializer_class = PriceEntrySerializer

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]